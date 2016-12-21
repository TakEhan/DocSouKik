#!/usr/bin/env python
#coding: utf-8
import RPi.GPIO as GPIO
import time

#通信用クラス
class skIRCOM:
    
    def plusValue(self,a,b):
        return a+b
    
    #定数定義（単位はsec)(ms以下は必ず少数指定)
    ON_USEC = 0.001
    OFF_USEC = 0.002
    STOP_USEC = 0.01
    READ_USEC = 0.01
    HIGH_USEC = 0.01
    
    #コンストラクタの生成
    def _init_(self,snd_pin_no,rcv_pin_no):
        GPIO.setmode(GPIO.BOARD)
        #送信ピンの設定
        self.SndPinNo = -1
        if snd_pin_no != -1:
            self.SndPinNo = snd_pin_no
        GPIO.setup(self.SndPinNo,GPIO.OUT)
        #受信ピンの設定
        self.RcvPinNo = -1
        if rcv_pin_no != 1:
            self.RcvPinNo = rcv_pin_no
        GPIO.setup(self.RcvPinNo,GPIO.IN)
         
    #パルスでは無いが名前そのまま
    #引数（秒）だけHIGH出力する
    #秒以下は少数指定
    def PalseHigh(self,cnt):
       GPIO.output(self.SndPinNo, GPIO.HIGH)
       time.sleep(cnt)
       GPIO.output(self.SndPinNo,GPIO.LOW)
       
    def DataCheck(self,MyDeviceNo,dt):
        #デバイスコードのチェック
        device = 0
        key1 = 0
        key2 = 0
        for n in range(8):
            if dt[n] == 1:
                device += 2**n
        if (device != 255) and (device != MyDeviceNo):
            return 0
        
        #キーデータ１のチェック
        for n in range(8):
            if dt[n+8] == 1:
                key1 += 2**n
        
        #キーデータ２のチェック
        for n in range(8):
            if dt[n+16] == 1:
                key2 += 2**n
        
        if key1 != key2:
            return 0
        return key1
                            
    #送信用メソッド
    def Send(self,toDeviceNo,KeyCode):
        #リーダ部を送る
        self.PalseHigh(0.05)
        time.sleep(self.READ_USEC)
        #デバイスコード送信
        for n in range(8):
            self.PalseHigh(self.HIGH_USEC)
            if (toDeviceNo >> n) & 0x1:
                time.sleep(self.ON_USEC)
            else:
                time.sleep(self.OFF_USEC)
        #キーデータ１を送る
        for n in range(8):
            self.PalseHigh(self.HIGH_USEC)
            if (KeyCode >> n) & 0x01:
                time.sleep(self.ON_USEC)
            else:
                time.sleep(self.OFF_USEC)
        #キーデータ１を反転して送る(確認用）
        for n in range(8):
            self.PalseHigh(self.HIGH_USEC)
            if (KeyCode >> n) & 0x01:
                time.sleep(self.OFF_USEC)
            else:
                time.sleep(self.ON_USEC)
        #ストップデータを送る
        self.PalseHigh(self.HIGH_USEC)
        time.sleep(self.STOP_USEC)
        
    #受信用メソッド
    def Recive(MyDeviceNo):
        ans = 0
        diff = 0
        IRbit = []
        #リーダ部のチェックを行う
        if GPIO.input(RcvPinNo)==LOW:
            t1 = datetime.now()
            while GPIO.input(RcvPinNo)==LOW:
                1#while文を書くため。意味は無い。書かなくても済むなら教えて。
            diff = datetime.now() -t1
                    
        if diff.miscroseconds >= 45000: #45msでリーダ部判定
            while GPIO.input(RcvPinNo) ==HIGH: #リーダ部を読み飛ばす
                1
            i = 0
            while True:
                while GPIO.input(RcvPinNo) ==LOW: #OFF部を読み飛ばす
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
                if i == 24: #3バイト読み込んだら終了
                    break
            
            if i == 24:
                ans = self.DataCheck(self.MyDeviceNo,IRbit)
            
            return ans