# -*- coding: utf-8 -*-
"""
Created on Sun May 08 17:33:13 2016

@author: adars
"""
import numpy as np

def describeByAge(s):
    
    length = len(s)
    count0to20 = np.zeros(shape=(8))
    count20to40 = np.zeros(shape=(8))
    count40to60 = np.zeros(shape=(8))
    count60to80 = np.zeros(shape=(8))
    count80 = np.zeros(shape=(8))
    7,8
    #t = s[0].split(',')
    #print t[7],t[8]
    
    for i in range(1,length):
        t = s[i].split(',')

        if int(t[7]) == 1:
            age = float(t[8])
        elif int(t[7]) == 2:
            age = float(t[8])/12.0
        
        if age >= 0.0 and age < 20.0:
            if t[19] == '0':
                count0to20[0] = count0to20[0]+1
            elif t[19] == '1':
                count0to20[1] = count0to20[1]+1
            elif t[19] == '2':
                count0to20[2] = count0to20[2]+1
            elif t[19] == '3':
                count0to20[3] = count0to20[3]+1
            elif t[19] == '4':
                count0to20[4] = count0to20[4]+1
            elif t[19] == '5':
                count0to20[5] = count0to20[5]+1
            elif t[19] == '6':
                count0to20[6] = count0to20[6]+1
            elif t[19] == '7':
                count0to20[7] = count0to20[7]+1
                
        elif age >= 20.0 and age < 40.0:
            if t[19] == '0':
                count20to40[0] = count20to40[0]+1
            elif t[19] == '1':
                count20to40[1] = count20to40[1]+1
            elif t[19] == '2':
                count20to40[2] = count20to40[2]+1
            elif t[19] == '3':
                count20to40[3] = count20to40[3]+1
            elif t[19] == '4':
                count20to40[4] = count20to40[4]+1
            elif t[19] == '5':
                count20to40[5] = count20to40[5]+1
            elif t[19] == '6':
                count20to40[6] = count20to40[6]+1
            elif t[19] == '7':
                count20to40[7] = count20to40[7]+1
                
        elif age >= 40.0 and age < 60.0:
            if t[19] == '0':
                count40to60[0] = count40to60[0]+1
            elif t[19] == '1':
                count40to60[1] = count40to60[1]+1
            elif t[19] == '2':
                count40to60[2] = count40to60[2]+1
            elif t[19] == '3':
                count40to60[3] = count40to60[3]+1
            elif t[19] == '4':
                count40to60[4] = count40to60[4]+1
            elif t[19] == '5':
                count40to60[5] = count40to60[5]+1
            elif t[19] == '6':
                count40to60[6] = count40to60[6]+1
            elif t[19] == '7':
                count40to60[7] = count40to60[7]+1
                
        elif age >= 60.0 and age < 80.0:
            if t[19] == '0':
                count60to80[0] = count60to80[0]+1
            elif t[19] == '1':
                count60to80[1] = count60to80[1]+1
            elif t[19] == '2':
                count60to80[2] = count60to80[2]+1
            elif t[19] == '3':
                count60to80[3] = count60to80[3]+1
            elif t[19] == '4':
                count60to80[4] = count60to80[4]+1
            elif t[19] == '5':
                count60to80[5] = count60to80[5]+1
            elif t[19] == '6':
                count60to80[6] = count60to80[6]+1
            elif t[19] == '7':
                count60to80[7] = count60to80[7]+1
                
        else:
            if t[19] == '0':
                count80[0] = count80[0]+1
            elif t[19] == '1':
                count80[1] = count80[1]+1
            elif t[19] == '2':
                count80[2] = count80[2]+1
            elif t[19] == '3':
                count80[3] = count80[3]+1
            elif t[19] == '4':
                count80[4] = count80[4]+1
            elif t[19] == '5':
                count80[5] = count80[5]+1
            elif t[19] == '6':
                count80[6] = count80[6]+1
            elif t[19] == '7':
                count80[7] = count80[7]+1
    """print "0 to 20", 
    for i in range(8):
        if i == 0:
            print "unspecified",count0to20[i]
        elif i ==1:
            print "Accident", count0to20[i]
        elif i ==2:
            print "Suicide", count0to20[i]
        elif i ==3:
            print "Homicide", count0to20[i]
        elif i ==4:
            print "Pending Investigation", count0to20[i]
        elif i ==5:
            print "Could not determine", count0to20[i]
        elif i ==6:
            print "Self-inflicted", count0to20[i]
        elif i ==7:
            print "Natural", count0to20[i]
    print "20 to 40", count20to40
    print "40 to 60", count40to60
    print "60 to 80", count60to80
    print "80 and above", count80
    """
    return count0to20,count20to40,count40to60,count60to80,count80