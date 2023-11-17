#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 12:44:18 2023

@author: gusweaver
"""

def fizz_buzz(input):
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0 :
        return "buzz"
    return input

print(fizz_buzz(3))






