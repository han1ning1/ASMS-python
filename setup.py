#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 22:45:23 2018

@author: hanning


"""
from distutils.core import setup,Extension

colotracker_module = Extension('_colotracker',
sources = ['colotracker_wrap.cxx','colotracker.cpp','histogram.cpp','region.cpp'])
setup(name = 'colotracker',
      version = '0.1',
      author = 'Hanning',
      description = 'ASMS Tracker',
      ext_modules = [colotracker_module],
      py_modules = ["colotracker"])
