# -*- coding: utf-8 -*-
import wx
#メモ帳のためだけのいらないもの
import os
#物質の通し番号（どうやって検索するのかよくわからないのでとりあえず）
global sortnumber
#初期値、最初の画面用
sortnumber=0


#1,3,4のボタンはメモ帳なので特に意味はない

#elseの中身はifの中身とほぼ変わらないので基本無視

#ボタンが四つついたやつのボタン、フレーム、パネルのサイズはすべてほぼ手動です

#globalは必要なときに書いているつもり

def click_button_1(event):
        os.system('notepad')
#ボタン２のイベント設定
def click_button_2(event):
    #wxでフレーム出すときに必要なやつ
    application = wx.App()
    
    #frameを定義して、作ったフレームを代入
    global frame1
    frame1 = List1()
    
    #中央に表示
    frame1.Centre()
    frame1.Show()
    
    #フレームを出すときに最後に書くやつ
    application.MainLoop()
    
#一つ目のリストのイベント設定（分類の選択用）
def listbox_select1(event):
    #押した選択肢を呼び出して代入
    obj = event.GetEventObject()
    
    #とりあえず一つだけ
    
    #表示されていた文字を呼び出す　
    if obj.GetStringSelection()=="element_1":
        
        #確認用、いらない
        print obj.GetStringSelection()
        
        application = wx.App()
        global frame2
        frame2 = List2()
        frame2.Centre()
        frame2.Show()
        application.MainLoop()
    else:
        print obj.GetStringSelection()
        
#二つ目のリストのイベント設定（物質の選択用）
def listbox_select2(event):
    obj=event.GetEventObject()
    global sortnumber
    if obj.GetStringSelection()=="element_1":
        
        #element_1なのでsortnumberを1に変更
        sortnumber=1
        
        #物質名を表示するのに使うために定義
        global name
        name=obj.GetStringSelection()
        
        #出ている三つのフレームをすべて消す（順番テキトー）
        global mframe
        frame1.Close()
        frame2.Close()
        mframe.Close()
        
        #ボタン四つの画面を再度表示（sortnumberで判断して画像を変える（CFrame内のif文））
        application = wx.App()
        mframe = CFrame()
        mframe.Centre()
        mframe.Show()
        application.MainLoop()
    else:
         name=obj.GetStringSelection()
         sortnumber=2
         frame1.Close()
         frame2.Close()
         mframe.Close()
         application = wx.App()
         mframe=CFrame()
         mframe.Centre()
         mframe.Show()
         application.MainLoop()
        
def click_button_3(event):
        os.system('notepad')
def click_button_4(event):
        os.system('notepad')


#一つ目のリスト（分類の選択用）の定義(だいたいこれと似たような感じ)
class List1(wx.Frame):
    def __init__(self):
        #フレームを定義（testはフレームの上部に出る名前）
        wx.Frame.__init__(self,None, wx.ID_ANY, u"test", size=(400,400))
        
        #パネルを定義
        panel = wx.Panel(self, wx.ID_ANY)
        #パネルの色を設定
        panel.SetBackgroundColour("#AFAFAF")
        
        #表示される要素を定義
        element_array = ("element_1", "element_2", "element_3", "element_4", "element_5", "element_6", "element_7", "element_8",
        "element_9", "element_10", "element_11", "element_12", "element_13", "element_14", "element_15")
        
        #listboxの定義、styleはスクロールの設定
        listbox_1 = wx.ListBox(panel, wx.ID_ANY, size=(400,400), choices=element_array, style=wx.LB_ALWAYS_SB)
        
        #イベントと関連づけ
        listbox_1.Bind(wx.EVT_LISTBOX, listbox_select1)
        
        #配置（boxsizerで配置、カッコ内は配置していく方向）
        layout = wx.BoxSizer(wx.HORIZONTAL)
        #flagはサイズの拡大方法、｜の後ろは余白の設定（テキトー）
        layout.Add(listbox_1, flag=wx.GROW | wx.ALL, border=3)
        
        #パネルのサイズをlayoutに合わせる
        panel.SetSizer(layout)

#二つ目のリスト（物質の選択用）の定義、一つ目と一緒
class List2(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,wx.ID_ANY, u"test", size=(400,400))
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("#AFAFAF")
        element_array = ("element_1", "element_2", "element_3", "element_4", "element_5", "element_6", "element_7", "element_8",
        "element_9", "element_10", "element_11", "element_12", "element_13", "element_14", "element_15")
        listbox_2 = wx.ListBox(panel, wx.ID_ANY, size=(400,400), choices=element_array, style=wx.LB_ALWAYS_SB)
        listbox_2.Bind(wx.EVT_LISTBOX, listbox_select2)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(listbox_2, flag=wx.GROW | wx.ALL, border=3)
        panel.SetSizer(layout)

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
        button_1 = wx.Button(self, wx.ID_ANY, u"1", size=(150,184))
        button_2  = wx.Button(self, wx.ID_ANY, u"2", size=(150,184))
        #上で定義したイベントと関連付け
        button_1.Bind(wx.EVT_BUTTON, click_button_1)
        button_2.Bind(wx.EVT_BUTTON, click_button_2)
        
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(button_1, flag=wx.GROW)
        layout.Add(button_2, flag=wx.GROW)
        self.SetSizer(layout)

#真ん中の画像と文字の表示部分
class CenterPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent,wx.ID_ANY,size=(480,400))
        global sortnumber
        #初期画面
        if sortnumber==0:
            #文章を作る、styleは文字を寄せる位置
            text = wx.StaticText(self, wx.ID_ANY, u"ブロックを設定してください", style=wx.TE_CENTER)
            
            #フォントの定義と適用、サイズは最初の数字、あとは不明
            font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            text.SetFont(font)
            
            #配置
            layout = wx.BoxSizer(wx.VERTICAL)
            layout.Add(text, flag=wx.GROW)
            self.SetSizer(layout)
            
        #sortnumberが1(element_1)のとき
        elif sortnumber==1:
            #画像を読み込む
            image = wx.Image('C:/Users/tanabe/Pictures/kongoueki.jpg')
            
            #bitmapにする、謎
            self.bitmap = image.ConvertToBitmap()
            
            #右辺はよくわからないけどなんかうまくいく
            gazou=wx.StaticBitmap(self, -1, self.bitmap)
            
            #文章を作る
            text = wx.StaticText(self, wx.ID_ANY, name, style=wx.TE_CENTER)
            font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            text.SetFont(font)
            
            #配置
            layout = wx.BoxSizer(wx.VERTICAL)
            layout.Add(text, flag=wx.GROW)
            layout.Add(gazou, flag=wx.GROW)
            self.SetSizer(layout)
        
        #写真を二つ横に配置するとき(要検討)
        elif sortnumber==2:
            image = wx.Image('C:/Users/tanabe/Pictures/kongoueki.jpg')
            self.bitmap = image.ConvertToBitmap()
            gazou1=wx.StaticBitmap(self, -1, self.bitmap)
            image = wx.Image('C:/Users/tanabe/Pictures/kongoueki.jpg')
            self.bitmap = image.ConvertToBitmap()
            gazou2=wx.StaticBitmap(self, -1, self.bitmap)
            text1 = wx.StaticText(self, wx.ID_ANY, name, style=wx.TE_CENTER)
            text2 = wx.StaticText(self, wx.ID_ANY, name, style=wx.TE_CENTER)
            font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            text1.SetFont(font)
            text2.SetFont(font)
            layout = wx.GridSizer(2,2)
            layout.Add(text1, flag=wx.SHAPED)
            layout.Add(text2, flag=wx.SHAPED)
            layout.Add(gazou1, flag=wx.GROW)
            layout.Add(gazou2, flag=wx.GROW)
            self.SetSizer(layout)
        
        #無視
        else:
            image = wx.Image('C:/Users/tanabe/Downloads/IMG_0432.jpg')
            self.bitmap = image.ConvertToBitmap()
            gazou=wx.StaticBitmap(self, -1, self.bitmap)
            text = wx.StaticText(self, wx.ID_ANY, u"中央寄せ", style=wx.TE_CENTER)
            font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            text.SetFont(font)
            layout = wx.BoxSizer(wx.VERTICAL)
            #layout.Add(gazou, flag=wx.GROW)
            layout.Add(text, flag=wx.GROW)
            self.SetSizer(layout)
       
class RightPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        button_3 = wx.Button(self, wx.ID_ANY, u"3", size=(150,184))
        button_4  = wx.Button(self, wx.ID_ANY, u"4", size=(150,184))
        button_3.Bind(wx.EVT_BUTTON, click_button_3)
        button_4.Bind(wx.EVT_BUTTON, click_button_4)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(button_3, flag=wx.GROW)
        layout.Add(button_4, flag=wx.GROW)
        self.SetSizer(layout)

#なんか書いてたから書いた
if __name__ == "__main__":
    
    application = wx.App()
    global mframe
    mframe = CFrame()
    mframe.Centre()
    mframe.Show()
    application.MainLoop()

