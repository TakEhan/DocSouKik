#!/usr/bin/env python
#coding: utf-8
import time

#�N���XskIRCOM�̌Ăяo���i�̃e�X�g�j
from InfraredCOM import skIRCOM
skIRCOM = skIRCOM()
#�Ăяo���̊m�F
answer = skIRCOM.plusValue(3,5)
print answer

#�ԊO���֘A���C�u�����̐���
skIRCOM._init_(32,33)

#�������Ɛݒ菈��
#time.sleep(5.0)#�T�b��ɑ��M�J�n

#���M����M���̐ݒ�
signal = [0,1,2]

#���C���̏����i�J�Ԃ����s�����j

counter = 0
while counter < 10:#�J�Ԃ��񐔂̐ݒ�
    for i in signal:
        KeyNo = signal[i]
        time.sleep(0.2)
        skIRCOM.Send(56,KeyNo)
        print KeyNo#�{���͕K�v�Ȃ��m�F
    time.sleep(1.0)    
    counter = counter + 1
"""
while True:
    ans = 0
    while ans == 0:
        KeyNo = skIRCOM.Recive(56)
    print ans
""" 