#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月8日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.AvatarLabel
@description: 
'''
from PyQt5.QtWidgets import QLabel


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class AvatarLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super(AvatarLabel, self).__init__(*args, **kwargs)