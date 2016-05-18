# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 18:58:15 2016

@author: adars
"""
import numpy as np

def describeByMaritalStatus(s):
    
    countS = np.zeros(shape=(8))
    countM = np.zeros(shape=(8))
    countW = np.zeros(shape=(8))
    countD = np.zeros(shape=(8))
    
    length = len(s)
    
    for i in range(1,length):
        t = s[i].split(',')
        
        if t[15] == 'S':
            if t[19] == '0':
                countS[0] = countS[0]+1
            elif t[19] == '1':
                countS[1] = countS[1]+1
            elif t[19] == '2':
                countS[2] = countS[2]+1
            elif t[19] == '3':
                countS[3] = countS[3]+1
            elif t[19] == '4':
                countS[4] = countS[4]+1
            elif t[19] == '5':
                countS[5] = countS[5]+1
            elif t[19] == '6':
                countS[6] = countS[6]+1
            elif t[19] == '7':
                countS[7] = countS[7]+1
        elif t[15] == 'M':
            if t[19] == '0':
                countM[0] = countM[0]+1
            elif t[19] == '1':
                countM[1] = countM[1]+1
            elif t[19] == '2':
                countM[2] = countM[2]+1
            elif t[19] == '3':
                countM[3] = countM[3]+1
            elif t[19] == '4':
                countM[4] = countM[4]+1
            elif t[19] == '5':
                countM[5] = countM[5]+1
            elif t[19] == '6':
                countM[6] = countM[6]+1
            elif t[19] == '7':
                countM[7] = countM[7]+1
        elif t[15] == 'W':
            if t[19] == '0':
                countW[0] = countW[0]+1
            elif t[19] == '1':
                countW[1] = countW[1]+1
            elif t[19] == '2':
                countW[2] = countW[2]+1
            elif t[19] == '3':
                countW[3] = countW[3]+1
            elif t[19] == '4':
                countW[4] = countW[4]+1
            elif t[19] == '5':
                countW[5] = countW[5]+1
            elif t[19] == '6':
                countW[6] = countW[6]+1
            elif t[19] == '7':
                countW[7] = countW[7]+1
        elif t[15] == 'M':
            if t[19] == '0':
                countM[0] = countM[0]+1
            elif t[19] == '1':
                countM[1] = countM[1]+1
            elif t[19] == '2':
                countM[2] = countM[2]+1
            elif t[19] == '3':
                countM[3] = countM[3]+1
            elif t[19] == '4':
                countM[4] = countM[4]+1
            elif t[19] == '5':
                countM[5] = countM[5]+1
            elif t[19] == '6':
                countM[6] = countM[6]+1
            elif t[19] == '7':
                countM[7] = countM[7]+1
        elif t[15] == 'D':
            if t[19] == '0':
                countD[0] = countD[0]+1
            elif t[19] == '1':
                countD[1] = countD[1]+1
            elif t[19] == '2':
                countD[2] = countD[2]+1
            elif t[19] == '3':
                countD[3] = countD[3]+1
            elif t[19] == '4':
                countD[4] = countD[4]+1
            elif t[19] == '5':
                countD[5] = countD[5]+1
            elif t[19] == '6':
                countD[6] = countD[6]+1
            elif t[19] == '7':
                countD[7] = countD[7]+1
                
    print "Number of deaths who were single:", countS
    print "Number of deaths who were Married:", countM
    print "Number of deaths who were widowed:", countW
    print "Number of deaths who were Divorced:", countD
    
    return countS,countM,countW,countD