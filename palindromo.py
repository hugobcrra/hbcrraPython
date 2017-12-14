#!/usr/bin/python
# -*- coding: utf-8 -*-
#Hgo Becerra
#UNAM-CERT

n = 'anitalavalatina'

def palindromo(n):
    if str(n) == str(n)[::-1]:
        print('True')
    else:
        print('False')
