#!/usr/bin/env python
#coding: utf-8
import RPi.GPIO as GPIO
import time

#�ʐM�p�N���X
class skIRCOM:
    
    def plusValue(self,a,b):
        return a+b
    
    #�萔��`�i�P�ʂ�sec)(ms�ȉ��͕K�������w��)
    ON_USEC = 0.001
    OFF_USEC = 0.002
    STOP_USEC = 0.01
    READ_USEC = 0.01
    HIGH_USEC = 0.01
    
    #�R���X�g���N�^�̐���
    def _init_(self,snd_pin_no,rcv_pin_no):
        GPIO.setmode(GPIO.BOARD)
        #���M�s���̐ݒ�
        self.SndPinNo = -1
        if snd_pin_no != -1:
            self.SndPinNo = snd_pin_no
        GPIO.setup(self.SndPinNo,GPIO.OUT)
        #��M�s���̐ݒ�
        self.RcvPinNo = -1
        if rcv_pin_no != 1:
            self.RcvPinNo = rcv_pin_no
        GPIO.setup(self.RcvPinNo,GPIO.IN)
         
    #�p���X�ł͖��������O���̂܂�
    #�����i�b�j����HIGH�o�͂���
    #�b�ȉ��͏����w��
    def PalseHigh(self,cnt):
       GPIO.output(self.SndPinNo, GPIO.HIGH)
       time.sleep(cnt)
       GPIO.output(self.SndPinNo,GPIO.LOW)
       
    def DataCheck(self,MyDeviceNo,dt):
        #�f�o�C�X�R�[�h�̃`�F�b�N
        device = 0
        key1 = 0
        key2 = 0
        for n in range(8):
            if dt[n] == 1:
                device += 2**n
        if (device != 255) and (device != MyDeviceNo):
            return 0
        
        #�L�[�f�[�^�P�̃`�F�b�N
        for n in range(8):
            if dt[n+8] == 1:
                key1 += 2**n
        
        #�L�[�f�[�^�Q�̃`�F�b�N
        for n in range(8):
            if dt[n+16] == 1:
                key2 += 2**n
        
        if key1 != key2:
            return 0
        return key1
                            
    #���M�p���\�b�h
    def Send(self,toDeviceNo,KeyCode):
        #���[�_���𑗂�
        self.PalseHigh(0.05)
        time.sleep(self.READ_USEC)
        #�f�o�C�X�R�[�h���M
        for n in range(8):
            self.PalseHigh(self.HIGH_USEC)
            if (toDeviceNo >> n) & 0x1:
                time.sleep(self.ON_USEC)
            else:
                time.sleep(self.OFF_USEC)
        #�L�[�f�[�^�P�𑗂�
        for n in range(8):
            self.PalseHigh(self.HIGH_USEC)
            if (KeyCode >> n) & 0x01:
                time.sleep(self.ON_USEC)
            else:
                time.sleep(self.OFF_USEC)
        #�L�[�f�[�^�P�𔽓]���đ���(�m�F�p�j
        for n in range(8):
            self.PalseHigh(self.HIGH_USEC)
            if (KeyCode >> n) & 0x01:
                time.sleep(self.OFF_USEC)
            else:
                time.sleep(self.ON_USEC)
        #�X�g�b�v�f�[�^�𑗂�
        self.PalseHigh(self.HIGH_USEC)
        time.sleep(self.STOP_USEC)
        
    #��M�p���\�b�h
    def Recive(MyDeviceNo):
        ans = 0
        diff = 0
        IRbit = []
        #���[�_���̃`�F�b�N���s��
        if GPIO.input(RcvPinNo)==LOW:
            t1 = datetime.now()
            while GPIO.input(RcvPinNo)==LOW:
                1#while�����������߁B�Ӗ��͖����B�����Ȃ��Ă��ςނȂ狳���āB
            diff = datetime.now() -t1
                    
        if diff.miscroseconds >= 45000: #45ms�Ń��[�_������
            while GPIO.input(RcvPinNo) ==HIGH: #���[�_����ǂݔ�΂�
                1
            i = 0
            while True:
                while GPIO.input(RcvPinNo) ==LOW: #OFF����ǂݔ�΂�
                    1
                t1 = datetime.now()
                while GPIO.input(RcvPinNo) ==HIGH:
                    1
                diff = datetime.now() - t1
                
                if diff.microseconds >= (self.ON_USEC*1000000):
                    IRbit.append(0)
                else:
                    IRbit.append(1)
                i += 1
                if i == 24: #3�o�C�g�ǂݍ��񂾂�I��
                    break
            
            if i == 24:
                ans = self.DataCheck(self.MyDeviceNo,IRbit)
            
            return ans