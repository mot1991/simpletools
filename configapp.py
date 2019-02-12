#!/usr/bin/python3
# -*- coding: utf-8 -*-

from baseapp import *

class ConfigApp(BaseApp):
    """docstring for ConfigApp"""
    def __init__(self, master = None):
        super(ConfigApp, self).__init__(master)
        # 设置窗口标题
        master.master.title('Auto Config Tool')
        self.pack()
        self._createWidgets()

    def _createWidgets(self):
        self.TabStrip1 = Notebook(self._group,
            width = app.M_APP_WIDTH, height = app.M_APP_HEIGHT)
    
        self.TabStrip1__Tab1 = Frame(self.TabStrip1)
        self.TabStrip1__Tab1Lbl = Label(self.TabStrip1__Tab1, text='Please add widgets in code.fff')
        self.TabStrip1__Tab1Lbl.pack()
        self.TabStrip1.add(self.TabStrip1__Tab1, text='aaaa')

        self.TabStrip1__Tab2 = Frame(self.TabStrip1)
        self.TabStrip1__Tab2Lbl = Label(self.TabStrip1__Tab2, text='Please add widgets in code.')
        self.TabStrip1__Tab2Lbl.pack()
        self.TabStrip1.add(self.TabStrip1__Tab2, text='bbbbb')

        self.TabStrip1.pack()

    def _menuCallback(self, *args, **kw):
        self.master.printToMsgBox('[ConfigApp] To config app.')