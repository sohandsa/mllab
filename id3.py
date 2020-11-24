import csv
import math
import random

def entropy(attributes,data,tar,attr):
    sum=0
    ent=0
    freq={}
    for entry in data:
         if entry[-1]==tar:
             pass
         elif entry[-1] in freq:
             freq[entry[-1]]+=1
         else:
            freq[entry[-1]]=1
    for item in freq.keys():
        sum+=freq[item]
    for item in freq.keys():
        val_prob=freq[item]/sum()
        ent+=-val_prob*math.log(val_prob,2)
    return ent ,item



def info_gain(attributes,data,tar,attr):
    sum=0
    freq={}
    j=0
    entropy_sum=0
    for i in attributes:
        if i==attr:
            break
        else:
            j=j+1
    for entry in data:
        if entry[j]==attr:
            pass
        elif entry[j] in freq:
            freq[entry[j]]+=1
            