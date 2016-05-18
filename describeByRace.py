# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 18:54:40 2016

@author: adars
"""
import numpy as np

def describeByRace(s):
    count0 = np.zeros(shape=(8))
    count1 = np.zeros(shape=(8))
    count2 = np.zeros(shape=(8))
    count3 = np.zeros(shape=(8))
    count4 = np.zeros(shape=(8))
    count5 = np.zeros(shape=(8))
    count6 = np.zeros(shape=(8))
    count7 = np.zeros(shape=(8))
    count8 = np.zeros(shape=(8))
    count9 = np.zeros(shape=(8))
    count10 = np.zeros(shape=(8))
    count11 = np.zeros(shape=(8))
    count12 = np.zeros(shape=(8))
    count13 = np.zeros(shape=(8))
    count14 = np.zeros(shape=(8))
    count15 = np.zeros(shape=(8))
    
    length = len(s)
    for i in range(1,length):
        t = s[i].split(',')
        if t[31] == '0':
            if t[19] == '0':
                count0[0] = count0[0]+1
            elif t[19] == '1':
                count0[1] = count0[1]+1
            elif t[19] == '2':
                count0[2] = count0[2]+1
            elif t[19] == '3':
                count0[3] = count0[3]+1
            elif t[19] == '4':
                count0[4] = count0[4]+1
            elif t[19] == '5':
                count0[5] = count0[5]+1
            elif t[19] == '6':
                count0[6] = count0[6]+1
            elif t[19] == '7':
                count0[7] = count0[7]+1
        elif t[31] == '1':
            if t[19] == '0':
                count1[0] = count1[0]+1
            elif t[19] == '1':
                count1[1] = count1[1]+1
            elif t[19] == '2':
                count1[2] = count1[2]+1
            elif t[19] == '3':
                count1[3] = count1[3]+1
            elif t[19] == '4':
                count1[4] = count1[4]+1
            elif t[19] == '5':
                count1[5] = count1[5]+1
            elif t[19] == '6':
                count1[6] = count1[6]+1
            elif t[19] == '7':
                count1[7] = count1[7]+1
        elif t[31] == '2':
            if t[19] == '0':
                count2[0] = count2[0]+1
            elif t[19] == '1':
                count2[1] = count2[1]+1
            elif t[19] == '2':
                count2[2] = count2[2]+1
            elif t[19] == '3':
                count2[3] = count2[3]+1
            elif t[19] == '4':
                count2[4] = count2[4]+1
            elif t[19] == '5':
                count2[5] = count2[5]+1
            elif t[19] == '6':
                count2[6] = count2[6]+1
            elif t[19] == '7':
                count2[7] = count2[7]+1
        elif t[31] == '3':
            if t[19] == '0':
                count3[0] = count3[0]+1
            elif t[19] == '1':
                count3[1] = count3[1]+1
            elif t[19] == '2':
                count3[2] = count3[2]+1
            elif t[19] == '3':
                count3[3] = count3[3]+1
            elif t[19] == '4':
                count3[4] = count3[4]+1
            elif t[19] == '5':
                count3[5] = count3[5]+1
            elif t[19] == '6':
                count3[6] = count3[6]+1
            elif t[19] == '7':
                count3[7] = count3[7]+1
        elif t[31] == '4':
            if t[19] == '0':
                count4[0] = count4[0]+1
            elif t[19] == '1':
                count4[1] = count4[1]+1
            elif t[19] == '2':
                count4[2] = count4[2]+1
            elif t[19] == '3':
                count4[3] = count4[3]+1
            elif t[19] == '4':
                count4[4] = count4[4]+1
            elif t[19] == '5':
                count4[5] = count4[5]+1
            elif t[19] == '6':
                count4[6] = count4[6]+1
            elif t[19] == '7':
                count4[7] = count4[7]+1
        elif t[31] == '5':
            if t[19] == '0':
                count5[0] = count5[0]+1
            elif t[19] == '1':
                count5[1] = count5[1]+1
            elif t[19] == '2':
                count5[2] = count5[2]+1
            elif t[19] == '3':
                count5[3] = count5[3]+1
            elif t[19] == '4':
                count5[4] = count5[4]+1
            elif t[19] == '5':
                count5[5] = count5[5]+1
            elif t[19] == '6':
                count5[6] = count5[6]+1
            elif t[19] == '7':
                count5[7] = count5[7]+1
        elif t[31] == '6':
            if t[19] == '0':
                count6[0] = count6[0]+1
            elif t[19] == '1':
                count6[1] = count6[1]+1
            elif t[19] == '2':
                count6[2] = count6[2]+1
            elif t[19] == '3':
                count6[3] = count6[3]+1
            elif t[19] == '4':
                count6[4] = count6[4]+1
            elif t[19] == '5':
                count6[5] = count6[5]+1
            elif t[19] == '6':
                count6[6] = count6[6]+1
            elif t[19] == '7':
                count6[7] = count6[7]+1
        elif t[31] == '7':
            if t[19] == '0':
                count7[0] = count7[0]+1
            elif t[19] == '1':
                count7[1] = count7[1]+1
            elif t[19] == '2':
                count7[2] = count7[2]+1
            elif t[19] == '3':
                count7[3] = count7[3]+1
            elif t[19] == '4':
                count7[4] = count7[4]+1
            elif t[19] == '5':
                count7[5] = count7[5]+1
            elif t[19] == '6':
                count7[6] = count7[6]+1
            elif t[19] == '7':
                count7[7] = count7[7]+1
        elif t[31] == '8':
            if t[19] == '0':
                count8[0] = count8[0]+1
            elif t[19] == '1':
                count8[1] = count8[1]+1
            elif t[19] == '2':
                count8[2] = count8[2]+1
            elif t[19] == '3':
                count8[3] = count8[3]+1
            elif t[19] == '4':
                count8[4] = count8[4]+1
            elif t[19] == '5':
                count8[5] = count8[5]+1
            elif t[19] == '6':
                count8[6] = count8[6]+1
            elif t[19] == '7':
                count8[7] = count8[7]+1
        elif t[31] == '18':
            if t[19] == '0':
                count9[0] = count9[0]+1
            elif t[19] == '1':
                count9[1] = count9[1]+1
            elif t[19] == '2':
                count9[2] = count9[2]+1
            elif t[19] == '3':
                count9[3] = count9[3]+1
            elif t[19] == '4':
                count9[4] = count9[4]+1
            elif t[19] == '5':
                count9[5] = count9[5]+1
            elif t[19] == '6':
                count9[6] = count9[6]+1
            elif t[19] == '7':
                count9[7] = count9[7]+1
        elif t[31] == '28':
            if t[19] == '0':
                count10[0] = count10[0]+1
            elif t[19] == '1':
                count10[1] = count10[1]+1
            elif t[19] == '2':
                count10[2] = count10[2]+1
            elif t[19] == '3':
                count10[3] = count10[3]+1
            elif t[19] == '4':
                count10[4] = count10[4]+1
            elif t[19] == '5':
                count10[5] = count10[5]+1
            elif t[19] == '6':
                count10[6] = count10[6]+1
            elif t[19] == '7':
                count10[7] = count10[7]+1
        elif t[31] == '38':
            if t[19] == '0':
                count11[0] = count11[0]+1
            elif t[19] == '1':
                count11[1] = count11[1]+1
            elif t[19] == '2':
                count11[2] = count11[2]+1
            elif t[19] == '3':
                count11[3] = count11[3]+1
            elif t[19] == '4':
                count11[4] = count11[4]+1
            elif t[19] == '5':
                count11[5] = count11[5]+1
            elif t[19] == '6':
                count11[6] = count11[6]+1
            elif t[19] == '7':
                count11[7] = count11[7]+1
        elif t[31] == '48':
            if t[19] == '0':
                count12[0] = count12[0]+1
            elif t[19] == '1':
                count12[1] = count12[1]+1
            elif t[19] == '2':
                count12[2] = count12[2]+1
            elif t[19] == '3':
                count12[3] = count12[3]+1
            elif t[19] == '4':
                count12[4] = count12[4]+1
            elif t[19] == '5':
                count12[5] = count12[5]+1
            elif t[19] == '6':
                count12[6] = count12[6]+1
            elif t[19] == '7':
                count12[7] = count12[7]+1
        elif t[31] == '58':
            if t[19] == '0':
                count13[0] = count13[0]+1
            elif t[19] == '1':
                count13[1] = count13[1]+1
            elif t[19] == '2':
                count13[2] = count13[2]+1
            elif t[19] == '3':
                count13[3] = count13[3]+1
            elif t[19] == '4':
                count13[4] = count13[4]+1
            elif t[19] == '5':
                count13[5] = count13[5]+1
            elif t[19] == '6':
                count13[6] = count13[6]+1
            elif t[19] == '7':
                count13[7] = count13[7]+1
        elif t[31] == '68':
            if t[19] == '0':
                count14[0] = count14[0]+1
            elif t[19] == '1':
                count14[1] = count14[1]+1
            elif t[19] == '2':
                count14[2] = count14[2]+1
            elif t[19] == '3':
                count14[3] = count14[3]+1
            elif t[19] == '4':
                count14[4] = count14[4]+1
            elif t[19] == '5':
                count14[5] = count14[5]+1
            elif t[19] == '6':
                count14[6] = count14[6]+1
            elif t[19] == '7':
                count14[7] = count14[7]+1
        elif t[31] == '78':
            if t[19] == '0':
                count15[0] = count15[0]+1
            elif t[19] == '1':
                count15[1] = count15[1]+1
            elif t[19] == '2':
                count15[2] = count15[2]+1
            elif t[19] == '3':
                count15[3] = count15[3]+1
            elif t[19] == '4':
                count15[4] = count15[4]+1
            elif t[19] == '5':
                count15[5] = count15[5]+1
            elif t[19] == '6':
                count15[6] = count15[6]+1
            elif t[19] == '7':
                count15[7] = count15[7]+1
                
    print "Deaths for Other races:", count0
    print "Deaths for White:", count1
    print "Deaths for Black:", count2
    print "Deaths for American Indian:", count3
    print "Deaths for Chinese:", count4
    print "Deaths for Japanese:", count5
    print "Deaths for Hawaiian:", count6
    print "Deaths for Filipino:", count7
    print "Deaths for Other Asian or Pacific Islander:", count8
    print "Deaths for Asian Indian:", count9
    print "Deaths for Korean:", count10
    print "Deaths for Samoan:", count11
    print "Deaths for Vietnamese:", count12
    print "Deaths for Guamanian:", count13
    print "Deaths for Other Asians or Pacific Islander in areas reporting codes 18-58:", count14
    print "Deaths for Combined other Asian or Pacific Islander, includes codes 18-68 for areas that do not report them separately:", count15
    
    return count0,count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,count13,count14,count15
         