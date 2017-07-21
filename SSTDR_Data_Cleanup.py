# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 08:32:22 2017

@author: jmajor
"""

#imports modules
import glob
import pandas as pd

#Input the file path for the date. Be suer to use double backslashes "\\"
filePath = 'C:\\Users\\jmajor\\Desktop\\SSTDR\\*.lwi'

#lists all files in path ending in .lwi
fileList = (glob.glob(filePath))

#This loop copies the metadata into new .csv files
for i in range(len(fileList)):
    f = open(fileList[i], 'r')
    z = f.read()
    z = z[:471]
    f.close()
    
    p = open('%s.csv' %fileList[i], 'w')
    p.write(z)
    p.write('\n\n')
    p.close()

#This loop appends the numerical data into the exsisting .csv files
for i in range(len(fileList)):
    x = pd.read_table(fileList[i], skiprows = 3)
    with open('%s.csv' %fileList[i], 'a') as f:
        x.to_csv(f, index = False)