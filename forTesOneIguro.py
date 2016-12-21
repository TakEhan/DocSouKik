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


#�{�^�����l������̃{�^���A�t���[���A�p�l���̃T�C�Y�͂��ׂĂقڎ蓮�ł�

#global�͕K�v�ȂƂ��ɏ����Ă������
#<<<<<startButtonEvents>>>>>
#<<<startStartEvent>>>���̃Z�N�V�������Ăяo�����O��realData�̐ݒ肪�K�v
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
    #wx�Ńt���[���o���Ƃ��ɕK�v�Ȃ��
    MenuApp = wx.App()
    
    #frame���`���āA������t���[������
    global MenuSortFrame
    MenuSortFrame = MenuSortList()
    
    #�����ɕ\��
    MenuSortFrame.Centre()
    MenuSortFrame.Show()
    
    #�t���[�����o���Ƃ��ɍŌ�ɏ������
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
#��ڂ̃��X�g�̃C�x���g�ݒ�i���ނ̑I��p�j
def MenuSortListBox(event):
    #�������I�������Ăяo���đ��
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

#��ڂ̃��X�g�̃C�x���g�ݒ�i�����̑I��p�j
def MenuIngListBox(event):
    obj=event.GetEventObject()
    
    #realData�ւ̑��
    #realData=obj.GetStringSelection()
    realData=obj.GetClientData(obj.Getselection())
    
    #�o�Ă���O�̃t���[�������ׂď����i���ԃe�L�g�[�j
    global MainFrame
    #MenuSortFrame.Close()
    #MenuIngFrame.Close()
    MainFrame.Close()
    
    #�{�^���l�̉�ʂ��ēx�\���irealData������Branch������iCFrame���ŏ����j�j
    MainApp = wx.App()
    MainFrame = CFrame()
    MainFrame.Centre()
    MainFrame.Show()
    MainApp.MainLoop()
#<<<<<endListEvents(in Menu)>>>>>


#<<<<<startDefineLists(in Menu)>>>>>
#��ڂ̃��X�g�i���ނ̑I��p�j�̒�`(������������Ǝ����悤�Ȋ���)
class MenuSortList(wx.Frame):
    def __init__(self):
        #�t���[�����`�itest�̓t���[���̏㕔�ɏo�閼�O�j
        wx.Frame.__init__(self,None, wx.ID_ANY, u"Sort", size=(350,350))
        
        #�p�l�����`
        panel = wx.Panel(self, wx.ID_ANY)
        #�p�l���̐F��ݒ�
        panel.SetBackgroundColour("#AFAFAF")
        
        #�\�������v�f���`�A�����͌������܂��Ă�����̂�\������Ηǂ��B
        #element_array = ("element_1", "element_2", "element_3", "element_4")
        
        #listbox�̒�`�Astyle�̓X�N���[���̐ݒ�
        SortListBox = wx.ListBox(panel, wx.ID_ANY, size=(350,350),  style=wx.LB_ALWAYS_SB)
        
        #elementArray�̑�ւƂ��āB���{�ꉻ
        SortListBox.Append(u",����1","element_1")
        SortListBox.Append(u",����2","element_2")
        SortListBox.Append(u",����3","element_3")
        SortListBox.Append(u",����4","element_4")
        #�C�x���g�Ɗ֘A�Â�
        SortListBox.Bind(wx.EVT_LISTBOX, MenuSortListBox)
        
        #�z�u�iboxsizer�Ŕz�u�A�J�b�R���͔z�u���Ă��������j
        layout = wx.BoxSizer(wx.HORIZONTAL)
        #flag�̓T�C�Y�̊g����@�A�b�̌��͗]���̐ݒ�i�e�L�g�[�j
        layout.Add(SortListBox, flag=wx.GROW | wx.ALL, border=3)
        
        #�p�l���̃T�C�Y��layout�ɍ��킹��
        panel.SetSizer(layout)

#��ڂ̃��X�g�i�����̑I��p�j�̒�`�A��ڂƈꏏ
class MenuIngList(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,wx.ID_ANY, u"Ingredients", size=(350,350))
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("#AFAFAF")
        global bunrui
        #�����̓��e�����ǂ��l���Ă��ω�����B�����Ƃ��Ď󂯎��ׂ���
        #element_array = ("forteskey", "element_2", "element_3")
        if bunrui=="element_1":
             SortListBox.Append(u",����1","forteskey")
             SortListBox.Append(u",����2","element_2")
             SortListBox.Append(u",����3","element_3")
             SortListBox.Append(u",����4","element_4")
             SortListBox.Append(u",����5","element_5")
        elif bunrui=="element_2":
             SortListBox.Append(u",����1","forteskey")
             SortListBox.Append(u",����2","element_2")
             SortListBox.Append(u",����3","element_3")
             SortListBox.Append(u",����4","element_4")
             SortListBox.Append(u",����5","element_5")
        elif bunrui=="element_3":
             SortListBox.Append(u",����1","forteskey")
             SortListBox.Append(u",����2","element_2")
             SortListBox.Append(u",����3","element_3")
             SortListBox.Append(u",����4","element_4")
             SortListBox.Append(u",����5","element_5")
        elif bunrui=="element_4":
             SortListBox.Append(u",����1","forteskey")
             SortListBox.Append(u",����2","element_2")
             SortListBox.Append(u",����3","element_3")
             SortListBox.Append(u",����4","element_4")
             SortListBox.Append(u",����5","element_5")
        
        IngListBox = wx.ListBox(panel, wx.ID_ANY, size=(350,350),  style=wx.LB_ALWAYS_SB)
        IngListBox.Bind(wx.EVT_LISTBOX, MenuIngListBox)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(IngListBox, flag=wx.GROW | wx.ALL, border=3)
        panel.SetSizer(layout)
#<<<<<endDefineLists(in Menu)>>>>>


#<<<<<startDefineMainFrame/Panel>>>>>
#�{�^���l�̂�̃t���[���̒�`�Aroot_panel�ɁA���ꂩ���`����O�̃p�l����z�u����A���E�̃p�l���̓{�^���̔z�u�̂�
class CFrame(wx.Frame):
    def __init__(self):
        #�t���[����`
        wx.Frame.__init__(self, None,wx.ID_ANY, u"test", size=(795,408),)
        
        #�p�l����`
        root_panel = wx.Panel(self, wx.ID_ANY)
        
        left_panel       = LeftPanel(root_panel)
        center_panel  = CenterPanel(root_panel)
        right_panel = RightPanel(root_panel)
        
        #�z�u
        root_layout = wx.BoxSizer(wx.HORIZONTAL)
        
        root_layout.Add(left_panel, 0, wx.GROW | wx.ALL)
        root_layout.Add(center_panel, 0, wx.GROW | wx.ALL)
        root_layout.Add(right_panel, 0, wx.GROW | wx.ALL)
        
        root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)
        

class LeftPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        #1,2�̓{�^���ɕ\������镶��
        StartButton = wx.Button(self, wx.ID_ANY, u"STAT", size=(210,203))
        MenuButton  = wx.Button(self, wx.ID_ANY, u"MENU", size=(210,203))
        #��Œ�`�����C�x���g�Ɗ֘A�t��
        StartButton.Bind(wx.EVT_BUTTON, StartClick)
        MenuButton.Bind(wx.EVT_BUTTON, MenuClick)
        
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(StartButton, flag=wx.GROW)
        layout.Add(MenuButton, flag=wx.GROW)
        self.SetSizer(layout)

#�^�񒆂̉摜�ƕ����̕\������
class CenterPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent,wx.ID_ANY,size=(480,400))
        global realData
        #�������
        if realData is "NA":
            #���͂����Astyle�͕������񂹂�ʒu
            text = wx.StaticText(self, wx.ID_ANY, u"�u���b�N��ݒ肵�Ă�������", style=wx.TE_CENTER)
            
            #�t�H���g�̒�`�ƓK�p�A�T�C�Y�͍ŏ��̐����A���Ƃ͕s��
            font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            text.SetFont(font)
            
            #�z�u
            layout = wx.BoxSizer(wx.VERTICAL)
            layout.Add(text, flag=wx.GROW)
            self.SetSizer(layout)
        
        #�����̉��͌���ł�realData�ɌʑΉ�����`�ŕ��򂾂��A����͂ł��Ȃ��B
        #�Ⴆ�΁A��z�u�̂Ƃ��ƈ�z�u�̂Ƃ��������򂷂���x�ɂ͂���ׂ��B
        #�v��{��
        else:
            #�摜��ǂݍ���
            image = wx.Image("picts/"+str(realData)+".jpg")
            
            #bitmap�ɂ���A��
            self.bitmap = image.ConvertToBitmap()
            
            #�E�ӂ͂悭�킩��Ȃ����ǂȂ񂩂��܂�����
            gazou=wx.StaticBitmap(self, -1, self.bitmap)
            
            #���͂����
            text = wx.StaticText(self, wx.ID_ANY, realData, style=wx.TE_CENTER)
            #should be Japanese(realData  is not Japanese)
            font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            text.SetFont(font)
            
            #�z�u
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
    
    #�萔�i�ł͂Ȃ����ǁj��`�i�P�ʂ�sec)(ms�ȉ��͕K�������w��)
    ON_USEC = 0.02
    OFF_USEC = 0.06
    STOP_USEC = 0.1
    READ_USEC = 0.1
    HIGH_USEC = 0.04
    
    SndPinNo  = 33
    RcvPinNo1 = 32 #��ʃI�����W��
    RcvPinNo2 = 40 #���ʃz���C�g��
    #<<<<<GPIOsettings>>>>>
    
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    #���M�s���̐ݒ�
    GPIO.setup(self.SndPinNo,GPIO.OUT)
    #��M�s���̐ݒ�
    GPIO.setup(self.RcvPinNo1,GPIO.IN)
    GPIO.setup(self.RcvPinNo2,GPIO.IN)
         
    #�p���X�ł͖��������O���̂܂�
    #�����i�b�j����HIGH�o�͂���
    #�b�ȉ��͏����w��
    def PalseHigh(self,cnt):
       GPIO.output(self.SndPinNo, GPIO.HIGH)
       time.sleep(cnt)
       GPIO.output(self.SndPinNo,GPIO.LOW)
    
    #�f�[�^�`�F�b�N
    def DataCheck(self,dt):
        key1 = 0
        key2 = 0
                
        #�L�[�f�[�^�P�̃`�F�b�N
        for n in range(8):
            if dt[n] == 1:
                key1 += 2**n
        print "key1 = ",key1
        
        #�L�[�f�[�^�Q�̃`�F�b�N
        for n in range(8):
            if dt[n+8] == 0:
                key2 += 2**n
        print "key2 = ",key2
        
        if key1 != key2:
            return 0
        else:
            return key1
                            
    #���M�p���\�b�h
    def Send(self,KeyCode):
        #���[�_���𑗂�
        self.PalseHigh(0.5)
        time.sleep(self.READ_USEC)
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
    def Recive(self):
        ans = 0
        t = 0
        IRbit = []
        #���[�_���̃`�F�b�N���s��
        if GPIO.input(self.RcvPinNo)==1:
            t1 = datetime.now()
            while GPIO.input(self.RcvPinNo)==1:
                1#while�����������߁B�Ӗ��͖����B�����Ȃ��Ă��ςނȂ狳���āB
            t2 = datetime.now()
            diff = t2 - t1
            t = diff.microseconds/1000
            
        if t >= 450: #450ms�Ń��[�_������
            print "Reader on"
            while GPIO.input(self.RcvPinNo) ==0: #���[�_����ǂݔ�΂�
                1
            i = 0
            while True:
                while GPIO.input(self.RcvPinNo) ==1: #OFF����ǂݔ�΂�
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
                if i == 16: #2�o�C�g�ǂݍ��񂾂�I��
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
    #�ő��M��M�ł���͂��B��M���ǂ��g�ݍ��ނ��s���Bwx.App.MainLoop�E�E�E
    #��M�ҋ@���[�h�ł�Reset���󂯓���Ȃ��Ƃ��Ȃ�MainLoop�ɓ��ꂸ�ɍςނ��ǁE�E�E
    global MainFrame
    MainFrame = CFrame()
    MainFrame.Centre()
    MainFrame.Show()
    MainApp.MainLoop()
#<<<<<endActualMainFlow>>>>>


#<<<<<===================>>>>>
#<<<<<========EOF========>>>>>
#<<<<<===================>>>>>





