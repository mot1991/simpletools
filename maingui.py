#!/usr/bin/python3
# -*- coding: utf-8 -*-

from baseapp import *
from configapp import *

class IndexApp(BaseApp):
    """docstring for IndexApp"""
    def __init__(self, master = None):
        super(IndexApp, self).__init__(master)
        # 设置窗口标题
        master.master.title('Index')
        Label(self._group, text = 'Index').pack()

    def _menuCallback(self, *args, **kw):
        self.master.printToMsgBox('[IndexApp] To index app.')


class MainApp(Frame):
    _curMenu = None

    """docstring for MainApp"""
    def __init__(self, master = None):
        super(MainApp, self).__init__(master)
        # 设置窗口标题
        self.master.title('Tools')
        # 设置窗口大小和位置（屏幕中间）
        width = app.M_APP_WIDTH
        height = app.M_APP_HEIGHT
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        xOffset = (screenWidth - width) // 2
        yOffset = (screenHeight - height) // 2
        alignstr = '{0}x{1}+{2}+{3}'.format(width, height, xOffset, yOffset)
        self.master.geometry(alignstr)
        # 设置窗口大小不可变
        self.master.resizable(width = False, height = False)
        # 设置窗口颜色
        self.master.config(bg = 'green')
        self.pack()
        
        # 创建菜单
        self._createMenus()
        self._createWidgets()

    def _createMenus(self):
        # 创建一个顶层菜单(工具)
        self._menuBar = Menu(self)
        # 创建默认菜单项(主页)
        self._toolMenu = Menu(self._menuBar, tearoff = False)
        for item in ['主页']:
            # 如果该菜单是顶层菜单的一个菜单项
            # 则它添加的是下拉菜单的菜单项
            self._toolMenu.add_command(label = item,
                    command = _mySetit(self, IndexApp, self._menuCallback))
        # 把菜单级联到顶层菜单上
        self._menuBar.add_cascade(label = "工具", menu = self._toolMenu)

        # 指定顶层菜单
        self.master.config(menu = self._menuBar)
    
    def _createWidgets(self):
        group = LabelFrame(self, text = "Message",
            width = app.MSG_APP_WIDTH, height = app.MSG_APP_HEIGHT)
        group.pack_propagate(0) # 使LabelFrame不随组件变化
        group.pack(side = BOTTOM, padx = 10, pady = 10)
        self._msgBox = ScrolledText(group)
        self._msgBox.pack(expand = 1, fill = "both")

    def _menuCallback(self, *args, **kw):
        pass

    def addMenuItem(self, *items):
        # 添加自定义菜单项
        self._menuList = items[:]
        for item in self._menuList:
            if 'name' in item:
                _label = item['name']
            else:
                _label = "未知"
            self._toolMenu.add_command(label = _label,
                    command = _mySetit(self, item['app'], self._menuCallback))
    
    def printToMsgBox(self, msg):
        if self._msgBox and type(msg) is str:
            self._msgBox.insert(END, msg + "\r\n")
        else:
            self._msgBox.insert(END, "[MainApp] Error\r\n")


class _mySetit:
    """Reference tkinter._setit, for MainApp only"""
    def __init__(self, mainapp, apptype, callback = None):
        self._mainapp = mainapp
        self._apptype = apptype 
        self._callback = callback

    def __call__(self, *args):
        curMenu = self._mainapp._curMenu
        if curMenu:
            curMenu.destroy()
        curMenu = self._mainapp._curMenu = self._apptype(self._mainapp)
        self._mainapp._curMenu.pack()
        if curMenu._menuCallback:
            curMenu._menuCallback(self._apptype, *args)
        elif self._callback:
            self._callback(self._apptype, *args) # TODO : 暂定


if __name__ == '__main__':
    tool = MainApp()
    # 自定义菜单项
    # 添加新的App时候 添加新的选项
    menuList = [
            {'name': '配置', 'app': ConfigApp},
        ]
    tool.addMenuItem(*menuList)
    # 主消息循环
    tool.mainloop()