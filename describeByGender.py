# -*- coding: utf-8 -*-
"""
Created on Thu May 12 01:47:01 2016

@author: adars
"""
import numpy as np

def describeByGender(s):
    length = len(s)
    countm = np.zeros(shape=(8))
    countf = np.zeros(shape=(8))
    for i in range(length-1):
        t = s[i+1].split(',')
        
        if t[6] == 'M':
            if t[19] == '0':
                countm[0] = countm[0]+1
            elif t[19] == '1':
                countm[1] = countm[1]+1
            elif t[19] == '2':
                countm[2] = countm[2]+1
            elif t[19] == '3':
                countm[3] = countm[3]+1
            elif t[19] == '4':
                countm[4] = countm[4]+1
            elif t[19] == '5':
                countm[5] = countm[5]+1
            elif t[19] == '6':
                countm[6] = countm[6]+1
            elif t[19] == '7':
                countm[7] = countm[7]+1
                
        else:
            if t[19] == '0':
                countf[0] = countf[0]+1
            elif t[19] == '1':
                countf[1] = countf[1]+1
            elif t[19] == '2':
                countf[2] = countf[2]+1
            elif t[19] == '3':
                countf[3] = countf[3]+1
            elif t[19] == '4':
                countf[4] = countf[4]+1
            elif t[19] == '5':
                countf[5] = countf[5]+1
            elif t[19] == '6':
                countf[6] = countf[6]+1
            elif t[19] == '7':
                countf[7] = countf[7]+1
    
    print "Male:", countm
    print "Female", countf
    
    return countm, countf