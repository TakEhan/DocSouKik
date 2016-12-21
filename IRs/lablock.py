#!/usr/bin/env python
#coding: utf-8
import time

#クラスskIRCOMの呼び出し（のテスト）
from InfraredCOM import skIRCOM
skIRCOM = skIRCOM()
#呼び出しの確認
answer = skIRCOM.plusValue(3,5)
print answer

#赤外線関連ライブラリの生成
skIRCOM._init_(32,33)

#初期化と設定処理
#time.sleep(5.0)#５秒後に送信開始

#送信する信号の設定
signal = [0,1,2]

#メインの処理（繰返し実行される）

counter = 0
while counter < 10:#繰返し回数の設定
    for i in signal:
        KeyNo = signal[i]
        time.sleep(0.2)
        skIRCOM.Send(56,KeyNo)
        print KeyNo#本来は必要ない確認
    time.sleep(1.0)    
    counter = counter + 1
"""
while True:
    ans = 0
    while ans == 0:
        KeyNo = skIRCOM.Recive(56)
    print ans
""" 