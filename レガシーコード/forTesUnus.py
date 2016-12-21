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
#from time import sleep
#for Picture
from PIL import Image
#for shutdown
import os
import sys
#for read csv files
import csv
#import pandas as pd
#<<<<<endInit>>>>>

#<<<<<startSetValues>>>>>
#temporarily disabled or permanently
#player = OMXPlayer('/home/pi/Desktop/ForTesUno.mp4')
STATID=1111
RSETID=3333
MENUID=2222
PoffID=4444
EnvDictionary='MvDict.csv'
ConvDictionary='CnvDict.csv'
element_array = ("element_1", "element_2", "element_3", "element_4")

#these two should be recieved another divice. 
#below things are just for test
realData="forteskey"
phantomData=00000000
movieName="ForTes"

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"test", size=(420,340))
frame.SetBackgroundColour("#000000")
MenuApp=wx.App()
MenuFrame=wx.Frame(frame, wx.ID_ANY, u"MENU", size=(200,200))
dict={}
dictCNV={}
#<<startCalcRelativePath>>
def relPath(pathpath):
    absoPath= os.path.dirname(os.path.abspath(__file__))
    os.path.normpath(os.path.join(absoPath,pathpath))
#<<endCalcRelativePath>>
#<<<<<endSetValues>>>>>


#<<<<<startDictInit>>>>>
#Conv realData>>moviePath
if os.path.exists(EnvDictionary) is False:
    with open(EnvDictionary,'ab') as tempTf:
        writer=csv.writer(tempTf,lineterminator='\n')
        writer.writerow([realData,movieName])
    print "NonExisting of the Dictionary"
with open(EnvDictionary,'rb') as tempF:
    tempDict=csv.reader(tempF)
    for row in tempDict:
        print "row: "
        print row
        dict[row[0]]=row[1]
#convdict phantomData>>realData
if os.path.exists(ConvDictionary) is False:
    with open(ConvDictionary,'ab') as tempTfC:
        writerC=csv.writer(tempTfC,lineterminator='\n')
        writerC.writerow([realData,phantomData])
    print "NonExisting of the Dictionary at CNV"
with open(ConvDictionary,'rb') as tempFC:
    tempDictConv=csv.reader(tempFC)
    for rowC in tempDictConv:
        dictCNV[rowC[0]]=rowC[1]
#<<<<<endDictInit>>>>>

#<<<<<startDefineFunctions>>>>>
#event when you push the button
def click_button(event):
    if event.GetId() == STATID:
        STATbutton.SetBackgroundColour("#0000FF")#JustForTest
        img=Image.open("picts/"+dict[realData]+".png")#load picture(Because OMXplayer takes a bit time)
        img.show()#show picture(it's not good way. it calls the normal app. on each OS)
        #<<<startPlaying>>>
        player = OMXPlayer("movs/"+dict[realData]+".mp4")
        player.play()
        time.sleep(3)
        player.pause()
        #if you got to quit you can't re-open
        player.quit()
    #<<<endPlaying>>>
    elif event.GetId() == MENUID:
        MENUbutton.SetBackgroundColour("#FF0000")
    #<<<startMenuWXsetUP>>>
        #MenuApp = wx.App()
        #MenuFrame = wx.Frame(None, wx.ID_ANY, u"MENU", size=(200,200))
        MenuPanel = wx.Panel(MenuFrame, wx.ID_ANY)
        MenuPanel.SetBackgroundColour("#AFAFAF")
    #<<startMakingListBox>>
        listbox_1 = wx.ListBox(MenuPanel, wx.ID_ANY, size=(200,200), choices=element_array, style=wx.LB_ALWAYS_SB)
        listbox_1.Bind(wx.EVT_LISTBOX, listbox_select)
    #<<endMakingListBox>>
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(listbox_1, flag=wx.GROW | wx.ALL, border=3)
        MenuPanel.SetSizer(layout)
    #<<<endMenuWXsetUP>>>
    #<<<startMenuDisp>>>
        MenuFrame.Show()
        MenuApp.MainLoop()
    #<<<endMenuDisp>>>
    elif event.GetId() == RSETID:
        STATbutton.SetBackgroundColour("AFAFAF")
        MENUbutton.SetBackgroundColour("AFAFAF")
        POFFbutton.SetBackgroundColour("AFAFAF")
    elif event.GetId() == PoffID:
        POFFbutton.SetBackgroundColour("#00FF00")
        frame.Close()
    #Close won't work now
        #Available below row, and system will be shuted down.
        #maybe we should show some confirmation
        #os.system("sudo shutdown -h now")
        sys.exit()
#event when you push menu
def listbox_select(event):
    obj = event.GetEventObject()
    print obj.GetStringSelection()
    #MenuFrame.Close() needs MenuFrame as Global
    MenuFrame.Close()
#<<<<<endDefineFunctions>>>>>

#<<<<<startWXsetUp>>>>>
#making Panel
panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("FF0000")

#set buttons  on the Panel
STATbutton = wx.Button(panel, STATID, u"STAT", size=(50,150))
RSETbutton = wx.Button(panel, RSETID, u"RSET", size=(50,150))
MENUbutton = wx.Button(panel, MENUID, u"MENU", size=(50,150))
POFFbutton = wx.Button(panel, PoffID, u"Poff", size=(50,150))

#wx.EVT_BUTTON calls above defined click_button()
frame.Bind(wx.EVT_BUTTON, click_button, STATbutton)
#it can go with STATbutton.Bind(wx.EVT_BUTTON, someNewFunction)
frame.Bind(wx.EVT_BUTTON, click_button, MENUbutton)
frame.Bind(wx.EVT_BUTTON, click_button, RSETbutton)
frame.Bind(wx.EVT_BUTTON, click_button, POFFbutton)

#set button Layout
layout = wx.GridSizer(2,2)
layout.Add(STATbutton,flag=wx.SHAPED | wx.ALIGN_LEFT)
layout.Add(MENUbutton,flag=wx.SHAPED | wx.ALIGN_RIGHT)
layout.Add(RSETbutton,flag=wx.SHAPED | wx.ALIGN_LEFT)
layout.Add(POFFbutton,flag=wx.SHAPED | wx.ALIGN_RIGHT)
panel.SetSizer(layout)
#<<<<<endWXsetUP>>>>>

#<<<<<startApplicationLoop>>>>>
frame.Show()
application.MainLoop()
#<<<<<endApplicationLoop>>>>>