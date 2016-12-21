# -*- coding: utf-8 -*-
import wx
import os
#eventCount=0
sortnumber=0
global name
name="a"

def click_button_1(event):
        os.system('notepad')
def click_button_2(event):
    #global eventCount
    #eventCount+=1
    #if eventCount%2==1:
    application = wx.App()
    global frame1
    frame1 = List1()
    frame1.Centre()
    frame1.Show()
    application.MainLoop()
    #else:
    #    frame1.Close()
def listbox_select1(event):
    obj = event.GetEventObject()
    if obj.GetStringSelection()=="element_1":
        print obj.GetStringSelection()
        application = wx.App()
        global frame2
        frame2 = List2()
        frame2.Centre()
        frame2.Show()
        application.MainLoop()
    else:
        print obj.GetStringSelection()
def listbox_select2(event):
    obj=event.GetEventObject()
    global sortnumber
    if obj.GetStringSelection()=="element_1":
        sortnumber=1
        global name
        name=obj.GetStringSelection()
        global mframe
        frame1.Close()
        frame2.Close()
        mframe.Close()
        application = wx.App()
        mframe = CFrame()
        mframe.Centre()
        mframe.Show()
        application.MainLoop()
        # mframe.SetStatusText(obj.GetStringSelection())
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

class List1(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None, wx.ID_ANY, u"test", size=(200,200))
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("#AFAFAF")
        element_array = ("element_1", "element_2", "element_3", "element_4", "element_5", "element_6", "element_7", "element_8",
        "element_9", "element_10", "element_11", "element_12", "element_13", "element_14", "element_15")
        listbox_1 = wx.ListBox(panel, wx.ID_ANY, size=(200,200), choices=element_array, style=wx.LB_ALWAYS_SB)
        listbox_1.Bind(wx.EVT_LISTBOX, listbox_select1)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(listbox_1, flag=wx.GROW | wx.ALL, border=3)
        panel.SetSizer(layout)

class List2(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,wx.ID_ANY, u"test", size=(200,200))
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("#AFAFAF")
        element_array = ("element_1", "element_2", "element_3", "element_4", "element_5", "element_6", "element_7", "element_8",
        "element_9", "element_10", "element_11", "element_12", "element_13", "element_14", "element_15")
        listbox_2 = wx.ListBox(panel, wx.ID_ANY, size=(200,200), choices=element_array, style=wx.LB_ALWAYS_SB)
        listbox_2.Bind(wx.EVT_LISTBOX, listbox_select2)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(listbox_2, flag=wx.GROW | wx.ALL, border=3)
        panel.SetSizer(layout)

class CFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,wx.ID_ANY, u"test", size=(416,323),)
        self.CreateStatusBar()
        self.SetStatusText(name)
        self.GetStatusBar().SetBackgroundColour(None)
        root_panel = wx.Panel(self, wx.ID_ANY)
        left_panel       = LeftPanel(root_panel)
        center_panel  = CenterPanel(root_panel)
        right_panel = RightPanel(root_panel)
        root_layout = wx.BoxSizer(wx.HORIZONTAL)
        root_layout.Add(left_panel, 0, wx.GROW | wx.ALL)
        root_layout.Add(center_panel, 0, wx.GROW | wx.ALL)
        root_layout.Add(right_panel, 0, wx.GROW | wx.ALL)
        root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)

class LeftPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        button_1 = wx.Button(self, wx.ID_ANY, "1", size=(50,130))
        button_2  = wx.Button(self, wx.ID_ANY, "2", size=(50,130))
        button_1.Bind(wx.EVT_BUTTON, click_button_1)
        button_2.Bind(wx.EVT_BUTTON, click_button_2)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(button_1, flag=wx.GROW)
        layout.Add(button_2, flag=wx.GROW)
        self.SetSizer(layout)

class CenterPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent,wx.ID_ANY,size=(300,300))
        global sortnumber
        if sortnumber==0:
            image = wx.Image('C:/Users/tanabe/Downloads/IMG_0432.jpg')
            self.bitmap = image.ConvertToBitmap()
            wx.StaticBitmap(self, -1, self.bitmap)
        if sortnumber==1:
            image = wx.Image('C:/Users/tanabe/Downloads/IMG_0431.jpg')
            self.bitmap = image.ConvertToBitmap()
            wx.StaticBitmap(self, -1, self.bitmap)
        else:
            image = wx.Image('C:/Users/tanabe/Downloads/IMG_0432.jpg')
            self.bitmap = image.ConvertToBitmap()
            wx.StaticBitmap(self, -1, self.bitmap)
        
       # wx.Panel.__init__(self, parent, wx.ID_ANY, size=(305,300))
       # button_a = wx.Button(self, wx.ID_ANY, "A", size=(200,30))
       # button_b  = wx.Button(self, wx.ID_ANY, "B", size=(200,30))
       # button_c = wx.Button(self, wx.ID_ANY, "C", size=(200,30))
       # button_d  = wx.Button(self, wx.ID_ANY, "D", size=(200,30))
       # button_e = wx.Button(self, wx.ID_ANY, "E", size=(200,30))
       # button_f  = wx.Button(self, wx.ID_ANY, "F", size=(200,30))
       # layout = wx.BoxSizer(wx.VERTICAL)
       # layout.Add(button_a, flag=wx.GROW)
       # layout.Add(button_b, flag=wx.GROW)
       # layout.Add(button_c, flag=wx.GROW)
       # layout.Add(button_d, flag=wx.GROW)
       # layout.Add(button_e, flag=wx.GROW)
       # layout.Add(button_f, flag=wx.GROW)
       # self.SetSizer(layout)
        
class RightPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        button_3 = wx.Button(self, wx.ID_ANY, "3", size=(50,130))
        button_4  = wx.Button(self, wx.ID_ANY, "4", size=(50,130))
        button_3.Bind(wx.EVT_BUTTON, click_button_3)
        button_4.Bind(wx.EVT_BUTTON, click_button_4)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(button_3, flag=wx.GROW)
        layout.Add(button_4, flag=wx.GROW)
        self.SetSizer(layout)
        
if __name__ == "__main__":
    application = wx.App()
    global mframe
    mframe = CFrame()
    mframe.Centre()
    mframe.Show()
    application.MainLoop()

