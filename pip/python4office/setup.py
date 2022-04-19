#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: python4office
# Mail: 1957875073@qq.com
# Created Time:  2022-1-5 10:17:34
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "python4office",      #这里是pip项目发布的名称
    version = "0.0.1",  #版本号，数值大的会优先被pip
    keywords = ("pip", "python4office"),
    description = "python for office",
    long_description = "",
    license = "MIT Licence",

    url = "http://python4office.cn/upload-pip/",     #项目相关文件地址，一般是github
    author = "python4office",
    author_email = "1957875073@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['pandas']          #这个项目需要的第三方库
)

