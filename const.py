#!/usr/bin/python3
# -*- coding: utf-8 -*-

class _const:
    '''常量'''
    class ConstError(TypeError) : pass

    def __setattr__(self, key, value):
        # self.__dict__
        if key in self.__dict__:
            raise self.ConstError("constant reassignment error!")
        self.__dict__[key] = value

import sys

sys.modules[__name__] = _const()