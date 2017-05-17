# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:20:39 2017

@author: zhangjiahao
"""
def getscore(name):
    sum=0;
    for i in range(len(name)):
        if(i>=1 and i<len(name)-1):
            temp=ord(name[i])-64;
            sum=sum+temp
    return sum;
    """define a new way to sort name at alphabetical order"""
def sortscore(name):
    sum=0;
    for i in range(len(name)):
        if(i>=1 and i<len(name)-1):
            temp=(ord(name[i])-64)*((1.0/26)**(i));
            sum=sum+temp
    return sum;
    """define the compare way to sort score"""
def comp(name1,name2):
    if sortscore(name1)>sortscore(name2):
        return 1;
    elif sortscore(name1)<sortscore(name2):
        return -1;
    else:
        return 0;
    