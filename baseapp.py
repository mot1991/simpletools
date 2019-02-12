#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
from constants import *

class BaseApp(Frame):
    """docstring for BaseApp"""
    def __init__(self, master = None):
        super(BaseApp, self).__init__(master)
        self._group = LabelFrame(self, text = "Tool",
            width = app.M_APP_WIDTH, height = app.M_APP_HEIGHT)
        self._group.pack_propagate(0) # 使LabelFrame不随组件变化
        self._group.pack(padx = 10, pady = 10)
