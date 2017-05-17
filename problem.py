# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import os
import namescore
file_my=open(os.getcwd()+'\p022_names.txt','r');
data=file_my.read().split(',');
data.sort(namescore.comp);
print namescore.getscore(data[937])
sum=0;
for i in range(len(data)):
    sum=(i+1)*namescore.getscore(data[i])+sum;
print sum