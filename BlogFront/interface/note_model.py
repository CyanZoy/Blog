# -*- coding: utf-8 -*-
"""
 @Time    : 2018/3/25 16:14
 @Author  : CyanZoy
 @File    : note_model.py
 @Describe: 提供查数据接口
 """
from BlogFront.models import *
from collections import defaultdict


class Change:
    @staticmethod
    def queryset_to_dic(*args, **kwargs):
        context = defaultdict(list)
        for _ in args:
            for i, j in zip(_, kwargs.values()):
                for k in i:
                    context[j].append(k)
        return context


class ModelGet:
    @staticmethod
    def note_get_t(name=None):
        """
        @ Create by CyanZoy on 2018/3/25 16:16
        @ Describe: 根据name-笔记本名获取相应笔记
        """
        try:
            if name:
                notename = NoteName.objects.get(name=name)
                return notename.belong_name.all().values()
            else:
                return NoteT.objects.all().values()
        except Exception as e:
            print(e)

    @staticmethod
    def note_get_name():
        """
        @ Create by CyanZoy on 2018/3/25 17:59
        @ Describe: 获取所有笔记类
        """
        try:
            return NoteName.objects.all().values()
        except Exception as e:
            print(e)


