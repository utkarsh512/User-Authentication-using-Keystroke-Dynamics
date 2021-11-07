import os
import string
from datetime import datetime
import numpy as np
import itertools
import pandas as pd
def mat(filename):
    ##########################################################

    lines = [line.rstrip('\t\n') for line in open(filename)]
    f_list = [event.split('\t') for event in lines]

    ##########################################################

    alp = list(string.ascii_lowercase)
    alp2 = list(map(''.join,itertools.combinations(string.ascii_lowercase,2)))

    ##########################################################

    def timediff(t1,t2):
        t1=(t1 + '000')
        t2=(t2 + '000')
        day1=datetime.strptime(t1, "%d:%m:%y:%H:%M:%S:%f")
        day2=datetime.strptime(t2, "%d:%m:%y:%H:%M:%S:%f")
        sec = (day2-day1).total_seconds()
        return(sec)

    ##########################################################
        
    KeyUps = [x for x in f_list if 'KeyUp' in x]
    KeyDowns = [x for x in f_list if 'KeyDown' in x]

    ###########################################################

    tups =  [item[2] for item in KeyUps]# if item[1] in alp]
    tdowns =  [item1[2] for item1 in KeyDowns]# if item1[1] in alp]
    try:
        letterup =  [item[1].upper() for item in KeyUps]# if item[1] in alp]
    except: 
        pass
        
    try:
        letterdown = [item1[1].upper() for item1 in KeyDowns]# if item1[1] in alp]
    except:
        pass
        
    #############################################################

    features = []
    for i in range(0,len(tups)-1):
        t = i

        t1 = tdowns[i]

        if letterup[t] != letterdown[i]:
            j = i
        
            if i == len(tups)-1:
                j = 0
            while j<len(tups)-1 and letterdown[i]!= letterup[j] and i!=len(tups)-1:
                j = j+1
        
            tj = tups[j]
            k = i
        
            if i == 0:
                k = len(tups)-1
            while k>=1 and letterdown[i]!= letterup[k] and i!=0:
                k = k-1
        
            tk = tups[k]
        
        
            if timediff(t1,tk)>0 and timediff(t1,tj)>0 :
                if abs(j-i)<abs(i-k):
                    t = j
                else:
                    t = k
        
            elif timediff(t1,tk)<0 :
                t = j
            else:
                t = k

        t2 = tups[t]
        
        

        if i!=len(tups)-1:
        
            t3 = tdowns[i+1]
            latency = timediff(t1,t3)
    
            lat = letterdown[i]+letterdown[i+1],latency
            features.append(lat)

        hold_time = timediff(t1,t2)
        hold = letterdown[i],hold_time
        features.append(hold)
        
    ###################################################################
    grid = [[[] for i in range(26)] for i in range(26)]
    grid1 = [[] for i in range(26)]
    for i in range(len(features)):
        if len(features[i][0]) == 2:
            if ord(features[i][0][0]) - ord('A') < 26 and ord(features[i][0][1]) - ord('A') < 26 and ord(features[i][0][1]) - ord('A') >= 0 and ord(features[i][0][0]) - ord('A') >= 0:
                #print(ord(features[i][0][0]) - ord('A'), ord(features[i][0][1]) - ord('A') )
                grid[ord(features[i][0][0]) - ord('A')][ord(features[i][0][1]) - ord('A')].append(features[i][1])
        elif len(features[i][0]) == 1:
            if ord(features[i][0]) - ord('A') < 26 and ord(features[i][0]) - ord('A') >= 0:
                grid1[ord(features[i][0]) - ord('A')].append(features[i][1])
    fin = [[0 for i in range(26)] for i in range(26)]
    fin1 = [0 for i in range(26)]
    for i in range(26):
        for j in range(26):
            fin[i][j] = sum(grid[i][j])
            if len(grid[i][j]) > 0:
                fin[i][j] /= len(grid[i][j])

    for i in range(26):

        fin1[i] = sum(grid1[i])
        if len(grid1[i]) > 0:
            fin1[i] /= len(grid1[i])
    return fin, fin1

doc = '5.txt'
fin, fin1 = mat(doc)


df = pd.DataFrame(fin)
df.to_csv('18EC10028/after_distances_28.csv', index = False)

df = pd.DataFrame(fin1)
df.to_csv('18EC10028/after_hold_28.csv', index = False)
