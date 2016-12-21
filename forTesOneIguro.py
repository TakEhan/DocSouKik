#!/usr/bin/env python
# -*- coding: utf-8 -*-


#!!!!!------------------------------------!!!!!
#    Execute this in "su", or it won't work
#!!!!!------------------------------------!!!!!


#<<<<<startInit>>>>>
#for Displaying; show some frames
import wx
#for GPIO(requiers sudo)
import RPi.GPIO as GPIO
#for showing movies
from omxplayer import OMXPlayer
#for sleep/time managing(time has sleep)
import time
#for Picture
#from PIL import Image
#for shutdown
import os
import sys
#for read csv files
import csv
#import pandas as pd
#for communication
from datetime import datetime
#<<<<<endInit>>>>>

#<<<<<startSetValues>>>>>
EnvDictionary='MvDict.csv'
ConvDictionary='CnvDict.csv'

#these two should be recieved from another divice.
#below things are just for test
realData="forteskey"
phantomData=00000000
movieName="ForTes"

dictRM={}#dict for RealData/MoviData
dictRP={}#dict for RealData/PhantomData

#<<startCalcRelativePath>>
def relPath(pathpath):
    absoPath= os.path.dirname(os.path.abspath(__file__))
    os.path.normpath(os.path.join(absoPath,pathpath))
#<<endCalcRelativePath>>
#<<<<<endSetValues>>>>>

#<<<<<startDictInit>>>>>
#<<Conv realData->moviePath>>
#<alter: NoDict>
if os.path.exists(EnvDictionary) is False:
    with open(EnvDictionary,'ab') as tempTf:
        #'a' means: make file unless it's already exist
        #'b' also has some meaning and you should use, but i don't now that
        writer=csv.writer(tempTf,lineterminator='\n')
        writer.writerow([realData,movieName])
    print "NonExisting of the Dictionary"
#<read the Dict>
with open(EnvDictionary,'rb') as tempF:
    tempDict=csv.reader(tempF)
    for row in tempDict:
        dictRM[row[0]]=row[1]

#<<Conv phantomData->realData>>
#<alter: NoDict>
if os.path.exists(ConvDictionary) is False:
    with open(ConvDictionary,'ab') as tempTfC:
        writerC=csv.writer(tempTfC,lineterminator='\n')
        writerC.writerow([realData,phantomData])
    print "NonExisting of the Dictionary at CNV"
#<read the Dict>
with open(ConvDictionary,'rb') as tempFC:
    tempDictConv=csv.reader(tempFC)
    for rowC in tempDictConv:
        dictRP[rowC[0]]=rowC[1]



#<<<<<endDictInit>>>>>


#ボタンが四つついたやつのボタン、フレーム、パネルのサイズはすべてほぼ手動です

#globalは必要なときに書いているつもり
#<<<<<startButtonEvents>>>>>
#<<<startStartEvent>>>このセクションが呼び出される前にrealDataの設定が必要
def StartClick(event):#forSTARTbutton:!!!!need be changed!!!!!!!!!!!!!
    StartButton.SetBackgroundColour("#0000FF")#JustForTest
    #<Playing>
    player = OMXPlayer("movs/"+dictRM[realData]+".mp4")
    player.play()
    time.sleep(3)
    player.pause()
    #if you got to quit you can't re-open
    player.quit()
#<<<endStartEvent>>>

#<<<startMenuEvent>>>
def MenuClick(event):
    #wxでフレーム出すときに必要なやつ
    MenuApp = wx.App()
    
    #frameを定義して、作ったフレームを代入
    global MenuSortFrame
    MenuSortFrame = MenuSortList()
    
    #中央に表示
    MenuSortFrame.Centre()
    MenuSortFrame.Show()
    
    #フレームを出すときに最後に書くやつ
    MenuApp.MainLoop()
#<<<endMenuEvent>>>

def ResetClick(event):
    StartButton.SetBackgroundColour("AFAFAF")
    MenuButton.SetBackgroundColour("AFAFAF")
    global realData
    realData="NA"
def PowerOffClick(event):
    frame.Close()
    #Close won't work now
    #Available below row, and system will be shuted down.
    #maybe we should show some confirmation
    #os.system("sudo shutdown -h now")
    sys.exit()
#<<<<<endButtonEvents>>>>>


#<<<<<startListEvents(in Menu)>>>>>NeedToEdit
#一つ目のリストのイベント設定（分類の選択用）
def MenuSortListBox(event):
    #押した選択肢を呼び出して代入
    obj = event.GetEventObject()
    global bunrui
    bunrui=obj.GetClientData(obj.Getselection())

    #startSort(needToBranch)
    #print obj.GetStringSelection()
    
    MenuIngApp = wx.App()
    global MenuIngFrame
    MenuIngFrame = MenuIngList()
    MenuIngFrame.Centre()
    MenuIngFrame.Show()
    MenuIngApp.MainLoop()

#二つ目のリストのイベント設定（物質の選択用）
def MenuIngListBox(event):
    obj=event.GetEventObject()
    
    #realDataへの代入
    #realData=obj.GetStringSelection()
    realData=obj.GetClientData(obj.Getselection())
    
    #出ている三つのフレームをすべて消す（順番テキトー）
    global MainFrame
    #MenuSortFrame.Close()
    #MenuIngFrame.Close()
    MainFrame.Close()
    
    #ボタン四つの画面を再度表示（realDataを元にBranchさせる（CFrame内で処理））
    MainApp = wx.App()
    MainFrame = CFrame()
    MainFrame.Centre()
    MainFrame.Show()
    MainApp.MainLoop()
#<<<<<endListEvents(in Menu)>>>>>


#<<<<<startDefineLists(in Menu)>>>>>
#一つ目のリスト（分類の選択用）の定義(だいたいこれと似たような感じ)
class MenuSortList(wx.Frame):
    def __init__(self):
        #フレームを定義（testはフレームの上部に出る名前）
        wx.Frame.__init__(self,None, wx.ID_ANY, u"Sort", size=(350,350))
        
        #パネルを定義
        panel = wx.Panel(self, wx.ID_ANY)
        #パネルの色を設定
        panel.SetBackgroundColour("#AFAFAF")
        
        #表示される要素を定義、ここは元来決まっているものを表示すれば良い。
        #element_array = ("element_1", "element_2", "element_3", "element_4")
        
        #listboxの定義、styleはスクロールの設定
        SortListBox = wx.ListBox(panel, wx.ID_ANY, size=(350,350),  style=wx.LB_ALWAYS_SB)
        
        #elementArrayの代替として。日本語化
        SortListBox.Append(u",分類1","element_1")
        SortListBox.Append(u",分類2","element_2")
        SortListBox.Append(u",分類3","element_3")
        SortListBox.Append(u",分類4","element_4")
        #イベントと関連づけ
        SortListBox.Bind(wx.EVT_LISTBOX, MenuSortListBox)
        
        #配置（boxsizerで配置、カッコ内は配置していく方向）
        layout = wx.BoxSizer(wx.HORIZONTAL)
        #flagはサイズの拡大方法、｜の後ろは余白の設定（テキトー）
        layout.Add(SortListBox, flag=wx.GROW | wx.ALL, border=3)
        
        #パネルのサイズをlayoutに合わせる
        panel.SetSizer(layout)

#二つ目のリスト（物質の選択用）の定義、一つ目と一緒
class MenuIngList(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,wx.ID_ANY, u"Ingredients", size=(350,350))
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("#AFAFAF")
        global bunrui
        #ここの内容物がどう考えても変化する。引数として受け取るべきか
        #element_array = ("forteskey", "element_2", "element_3")
        if bunrui=="element_1":
             SortListBox.Append(u",物質1","forteskey")
             SortListBox.Append(u",物質2","element_2")
             SortListBox.Append(u",物質3","element_3")
             SortListBox.Append(u",物質4","element_4")
             SortListBox.Append(u",物質5","element_5")
        elif bunrui=="element_2":
             SortListBox.Append(u",物質1","forteskey")
             SortListBox.Append(u",物質2","element_2")
             SortListBox.Append(u",物質3","element_3")
             SortListBox.Append(u",物質4","element_4")
             SortListBox.Append(u",物質5","element_5")
        elif bunrui=="element_3":
             SortListBox.Append(u",物質1","forteskey")
             SortListBox.Append(u",物質2","element_2")
             SortListBox.Append(u",物質3","element_3")
             SortListBox.Append(u",物質4","element_4")
             SortListBox.Append(u",物質5","element_5")
        elif bunrui=="element_4":
             SortListBox.Append(u",物質1","forteskey")
             SortListBox.Append(u",物質2","element_2")
             SortListBox.Append(u",物質3","element_3")
             SortListBox.Append(u",物質4","element_4")
             SortListBox.Append(u",物質5","element_5")
        
        IngListBox = wx.ListBox(panel, wx.ID_ANY, size=(350,350),  style=wx.LB_ALWAYS_SB)
        IngListBox.Bind(wx.EVT_LISTBOX, MenuIngListBox)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(IngListBox, flag=wx.GROW | wx.ALL, border=3)
        panel.SetSizer(layout)
#<<<<<endDefineLists(in Menu)>>>>>


#<<<<<startDefineMainFrame/Panel>>>>>
#ボタン四つのやつのフレームの定義、root_panelに、これから定義する三つのパネルを配置する、左右のパネルはボタンの配置のみ
class CFrame(wx.Frame):
    def __init__(self):
        #フレーム定義
        wx.Frame.__init__(self, None,wx.ID_ANY, u"test", size=(795,408),)
        
        #パネル定義
        root_panel = wx.Panel(self, wx.ID_ANY)
        
        left_panel       = LeftPanel(root_panel)
        center_panel  = CenterPanel(root_panel)
        right_panel = RightPanel(root_panel)
        
        #配置
        root_layout = wx.BoxSizer(wx.HORIZONTAL)
        
        root_layout.Add(left_panel, 0, wx.GROW | wx.ALL)
        root_layout.Add(center_panel, 0, wx.GROW | wx.ALL)
        root_layout.Add(right_panel, 0, wx.GROW | wx.ALL)
        
        root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)
        

class LeftPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        #1,2はボタンに表示される文字
        StartButton = wx.Button(self, wx.ID_ANY, u"STAT", size=(210,203))
        MenuButton  = wx.Button(self, wx.ID_ANY, u"MENU", size=(210,203))
        #上で定義したイベントと関連付け
        StartButton.Bind(wx.EVT_BUTTON, StartClick)
        MenuButton.Bind(wx.EVT_BUTTON, MenuClick)
        
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(StartButton, flag=wx.GROW)
        layout.Add(MenuButton, flag=wx.GROW)
        self.SetSizer(layout)

#真ん中の画像と文字の表示部分
class CenterPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent,wx.ID_ANY,size=(480,400))
        global realData
        #初期画面
        if realData is "NA":
            #文章を作る、styleは文字を寄せる位置
            text = wx.StaticText(self, wx.ID_ANY, u"ブロックを設定してください", style=wx.TE_CENTER)
            
            #フォントの定義と適用、サイズは最初の数字、あとは不明
            font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            text.SetFont(font)
            
            #配置
            layout = wx.BoxSizer(wx.VERTICAL)
            layout.Add(text, flag=wx.GROW)
            self.SetSizer(layout)
        
        #ここの下は現状ではrealDataに個別対応する形で分岐だが、それはできない。
        #例えば、二つ配置のときと一つ配置のときだけ分岐する程度にはするべき。
        #要一本化
        else:
            #画像を読み込む
            image = wx.Image("picts/"+str(realData)+".jpg")
            
            #bitmapにする、謎
            self.bitmap = image.ConvertToBitmap()
            
            #右辺はよくわからないけどなんかうまくいく
            gazou=wx.StaticBitmap(self, -1, self.bitmap)
            
            #文章を作る
            text = wx.StaticText(self, wx.ID_ANY, realData, style=wx.TE_CENTER)
            #should be Japanese(realData  is not Japanese)
            font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            text.SetFont(font)
            
            #配置
            layout = wx.BoxSizer(wx.VERTICAL)
            layout.Add(text, flag=wx.GROW)
            layout.Add(gazou, flag=wx.GROW)
            self.SetSizer(layout)
        
       
class RightPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        ResetButton = wx.Button(self, wx.ID_ANY, u"RSET", size=(210,203))
        PowerOffButton  = wx.Button(self, wx.ID_ANY, u"Poff", size=(210,203))
        ResetButton.Bind(wx.EVT_BUTTON, ResetClick)
        PowerOffButton.Bind(wx.EVT_BUTTON, PowerOffClick)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(ResetButton, flag=wx.GROW)
        layout.Add(PowerOffButton, flag=wx.GROW)
        self.SetSizer(layout)
#<<<<<endDefineMainFrame/Panel>>>>>
#<<<<<Communication>>>>>
class Com:
    
    #定数（ではないけど）定義（単位はsec)(ms以下は必ず少数指定)
    ON_USEC = 0.02
    OFF_USEC = 0.06
    STOP_USEC = 0.1
    READ_USEC = 0.1
    HIGH_USEC = 0.04
    
    SndPinNo  = 33
    RcvPinNo1 = 32 #上面オレンジ線
    RcvPinNo2 = 40 #下面ホワイト線
    #<<<<<GPIOsettings>>>>>
    
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    #送信ピンの設定
    GPIO.setup(self.SndPinNo,GPIO.OUT)
    #受信ピンの設定
    GPIO.setup(self.RcvPinNo1,GPIO.IN)
    GPIO.setup(self.RcvPinNo2,GPIO.IN)
         
    #パルスでは無いが名前そのまま
    #引数（秒）だけHIGH出力する
    #秒以下は少数指定
    def PalseHigh(self,cnt):
       GPIO.output(self.SndPinNo, GPIO.HIGH)
       time.sleep(cnt)
       GPIO.output(self.SndPinNo,GPIO.LOW)
    
    #データチェック
    def DataCheck(self,dt):
        key1 = 0
        key2 = 0
                
        #キーデータ１のチェック
        for n in range(8):
            if dt[n] == 1:
                key1 += 2**n
        print "key1 = ",key1
        
        #キーデータ２のチェック
        for n in range(8):
            if dt[n+8] == 0:
                key2 += 2**n
        print "key2 = ",key2
        
        if key1 != key2:
            return 0
        else:
            return key1
                            
    #送信用メソッド
    def Send(self,KeyCode):
        #リーダ部を送る
        self.PalseHigh(0.5)
        time.sleep(self.READ_USEC)
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
    def Recive(self):
        ans = 0
        t = 0
        IRbit = []
        #リーダ部のチェックを行う
        if GPIO.input(self.RcvPinNo)==1:
            t1 = datetime.now()
            while GPIO.input(self.RcvPinNo)==1:
                1#while文を書くため。意味は無い。書かなくても済むなら教えて。
            t2 = datetime.now()
            diff = t2 - t1
            t = diff.microseconds/1000
            
        if t >= 450: #450msでリーダ部判定
            print "Reader on"
            while GPIO.input(self.RcvPinNo) ==0: #リーダ部を読み飛ばす
                1
            i = 0
            while True:
                while GPIO.input(self.RcvPinNo) ==1: #OFF部を読み飛ばす
                    1
                t1 = datetime.now()
                while GPIO.input(self.RcvPinNo) ==0:
                    1
                t2 = datetime.now()
                diff = t2 - t1
                t = diff.microseconds/1000
                if t >= 40:
                    IRbit.append(0)
                else:
                    IRbit.append(1)
                i += 1
                if i == 16: #2バイト読み込んだら終了
                    break
            print IRbit
            
            if i == 16:
                print "check start"
                ans = self.DataCheck(MyDeviceNo,IRbit)
            
            return ans


#<<<<<startActualMainFlow>>>>>
if __name__ == "__main__":
    MainApp = wx.App()
    com = Com()
    #com.Send(int)
    #com.Recive()
    #で送信受信できるはず。受信をどう組み込むか不明。wx.App.MainLoop・・・
    #受信待機モードではResetも受け入れないとかならMainLoopに入れずに済むけど・・・
    global MainFrame
    MainFrame = CFrame()
    MainFrame.Centre()
    MainFrame.Show()
    MainApp.MainLoop()
#<<<<<endActualMainFlow>>>>>


#<<<<<===================>>>>>
#<<<<<========EOF========>>>>>
#<<<<<===================>>>>>





