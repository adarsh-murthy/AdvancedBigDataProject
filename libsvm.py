# -*- coding: utf-8 -*-
"""
Created on Mon May 09 05:26:58 2016

@author: adars
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:12:31 2016

@author: adars
"""

from sklearn import linear_model
from sklearn import svm
import numpy as np

def getData(icd):
    txt = open("DeathRecords.csv",'r')
    s = txt.readlines()
    txt.close()
    
    datatemp = np.zeros(shape=(len(s)-1,12))
    mannerOfDeath = np.zeros(shape=(len(s)-1))
    
    for i in range(0,len(s)-1):
        t = s[i+1].split(',')
        datatemp[i][0] = int(t[1])-1
        if int(t[2]) == 99:
            datatemp[i][1] = 18
        else:
            datatemp[i][1] = t[2]
        if int(t[3]) == 0:
            datatemp[i][2] = 0
        else:
            datatemp[i][2] = int(t[3]) - 1
        if t[6] == 'M':
            datatemp[i][3] = 0
        else:
            datatemp[i][3] = 1
        if int(t[7]) == 4:
            datatemp[i][4] = 2
        elif int(t[7]) == 5:
            datatemp[i][4] = 3
        elif int(t[7]) == 6:
            datatemp[i][4] = 4
        elif int(t[7]) == 9:
            datatemp[i][4] = 5
        else:
            datatemp[i][4] = int(t[7]) - 1
        datatemp[i][5] = t[8]
        if int(t[14]) == 9:
            datatemp[i][6] = 7
        else:
            datatemp[i][6] = int(t[14]) - 1
        if t[15] == 'S':
            datatemp[i][7] = 0
        elif t[15] == 'M':
            datatemp[i][7] = 1
        elif t[15] == 'D':
            datatemp[i][7] = 2
        else:
            datatemp[i][7] = 3
        
        if t[18] == 'U':
            datatemp[i][8] = 2
        elif t[18] == 'Y':
            datatemp[i][8] = 1
        else:
            datatemp[i][8] = 0
        if int(t[31]) == 18:
            datatemp[i][9] = 9
        elif int(t[31]) == 28:
            datatemp[i][9] = 10
        elif int(t[31]) == 38:
            datatemp[i][9] = 11
        elif int(t[31]) == 48:
            datatemp[i][9] = 12
        elif int(t[31]) == 58:
            datatemp[i][9] = 13
        elif int(t[31]) == 68:
            datatemp[i][9] = 14
        elif int(t[31]) == 78:
            datatemp[i][9] = 15
        else:
            datatemp[i][9] = t[31]
        if int(t[22]) == 8:
            datatemp[i][10] = 5
        elif int(t[22]) == 9:
            datatemp[i][10] = 6
        elif int(t[22]) == 99:
            datatemp[i][10] = 7
        else:
            datatemp[i][10] = t[22]
        if int(t[23]) == 99:
            datatemp[i][11] = 10
        else:
            datatemp[i][11] = t[23]
        #for z in range(len(icd)-1):
        #    dis = icd[z+1].split(',')
        #    if t[24] == dis[0]:
        #        datatemp[i][12] = z
        #        break
        
        
        mannerOfDeath[i] = t[19]
    return mannerOfDeath, datatemp
        
def createLibsvm(datatemp,mannerOfDeath,samples):
    txt = open("datanewagain.txt",'w')
    for i in range(samples):
        line = str(int(mannerOfDeath[i])) + " " 
        t = datatemp[i]
        for j in range(12):
            if j < 11:
                line = line + str(j+1) + ":" + str(int(t[j])) + " "
            else:
                line = line + str(j+1) + ":" + str(int(t[j])) + "\n"
        txt.write(line)
    txt.close()

def icd10():
    txt = open("Icd10Code.csv", 'r')
    s = txt.readlines()
    txt.close()
    return s

icd = icd10()
label,data = getData(icd)
createLibsvm(data,label,len(data))

