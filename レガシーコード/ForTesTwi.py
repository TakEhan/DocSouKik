#!/usr/bin/env python
#coding: utf-8

import commands
import RPi.GPIO as GPIO
import time

#まず、起動後はここが走る。
#initialize: 
#変数の準備は必要ないので、ここで行われるのは、画面の用意。
import wx
 
#Statof: http://www.blog.pythonlibrary.org/2013/07/12/wxpython-making-your-frame-maximize-or-full-screen/
########################################################################
class MyPanel(wx.Panel):
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        #Constructor
        wx.Panel.__init__(self, parent)
 
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
 
    #----------------------------------------------------------------------
    def onKey(self, event):
        #Check for ESC key press and exit is ESC is pressed
        
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.GetParent().Close()
        else:
            event.Skip()
 
 
########################################################################
class MyFrame(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        #Constructor, wx.Frameでは引数としてタイトルの後にサイズを取ることができる。
        wx.Frame.__init__(self, None, title="Test FullScreen")
        root_panel = MyPanel(self)
        self.ShowFullScreen(True)
        #Statof: http://www.python-izm.com/contents/gui/layout_concept.shtml
        #    本体部分の構築
        root_panel = wx.Panel(self, wx.ID_ANY)

        text_panel       = TextPanel(root_panel)
        calcbutton_panel = CalcButtonPanel(root_panel)
        lMenu_p=LeftMenuPanel(root_panel)
        rMenu_p=RightMenuPanel(root_panel)

        root_layout = wx.BoxSizer(wx.HORIZONTAL)
        root_layout.Add(lMenu_p,0,flag=wx.SHAPED | wx.RIGHT, border=100)
        root_layout.Add(rMenu_p,0,flag=wx.SHAPED | wx.LEFT, border=100)
        root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)
        #ここまでフレームクラス内部Endof: http://www.python-izm.com/contents/gui/layout_concept.shtml

#ここからが本文にである。この前はクラスである。
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
#Endof: http://www.blog.pythonlibrary.org/2013/07/12/wxpython-making-your-frame-maximize-or-full-screen/
#ここまでで、画面はフルスクリーン化されているはず。

#メニューの表示（メニュー画面に戻るのはここ）
#メニューによる入力を受け付ける

#Statof: http://www.python-izm.com/contents/gui/layout_concept.shtml
#--------------------------------------
#    画面上部に表示されるテキスト部分
#--------------------------------------
class TextPanel(wx.Panel):

    def __init__(self,parent):
    
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        
        calc_text = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_RIGHT)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(calc_text, 1)
        self.SetSizer(layout)


#--------------------------------------
#    画面下部に表示されるボタン部分
#--------------------------------------

class LeftMenuPanel(wx.Panel):
    def __init__(self,parent):
        wxPanel.__init__(self,parent,wx.ID_ANY)
        
        layout=wx.GridSizer(1,2)
        layout.Add(wx.Button(self,wx.ID_ANY,u"STAT",size=(30,25)),1,wx.ALIGN_TOP)
        layout.Add(wx.Button(self,wx.ID_ANY,u"RSET",size=(30,25)),1,wx.ALIGN_BOTTOM)
        

class RightMenuPanel(wx.Panel):
    def __init__(self,parent):
        wxPanel.__init__(self,parent,wx.ID_ANY)
        
        layout=wx.GridSizer(1,2)
        layout.Add(wx.Button(self,wx.ID_ANY,u"MENU",size=(30,25)),1,wx.ALIGN_TOP)
        layout.Add(wx.Button(self,wx.ID_ANY,u"Poff",size=(30,25)),1,wx.ALIGN_BOTTOM)
#ENDof: http://www.python-izm.com/contents/gui/layout_concept.shtml

#設定後、画像画面へ遷移

#画像画面描画（リセットはここに戻る。）
#画像画面では、トリガ、メニュー画面への戻り、リセット（導入物質の破棄と、画像画面の初期化）、パワーオフがサポートされる。

#待ち受け開始
#外部入力からの処理
#トリガの処理（外部入力からの処理と一部同一。）
#ディスプレイへの表示（映像の選択と再生）
temp=commands.getoutput("mplayer /home/pi/Desktop/tes2.mp4 -geometry 0:0")
print temp
#外部入力からの処理ここまで
#待ち受け終了

#パワーオフの処理
