#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Auther: Big Vegetable
# @Time: ----11\18\2019

class Settings(object):
    """储存《外星人入侵》的所有设置类"""
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 200, 200)
        #飞船的位置
        self.ship_speed_factor = 2.5

if __name__ == "__main__":
    pass

