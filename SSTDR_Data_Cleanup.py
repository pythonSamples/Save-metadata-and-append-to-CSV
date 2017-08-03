'''
You must create two folders in the directory with the .lwi files
folder 1: csv_files
folder 2: averages
'''


#imports modules
import glob
import pandas as pd
import os


filePath = '*.lwi' #used to find all files ending in .lwi
cwd = os.getcwd() #current directory

fileList = (glob.glob(filePath)) #lists all files in the curernt file path ending in .lwi

#This loop copies the metadata into new .csv files
for i in range(len(fileList)):
    f = open(fileList[i], 'r')
    z = f.read()
    z = z[:471]
    f.close()
    
    
    p = open('%s\\csv_files\\%s.csv' %(cwd,fileList[i][0:35]), 'w')
    p.write(z)
    p.write('\n\n')
    p.close()

#This loop appends the numerical data into the exsisting .csv files
for i in range(len(fileList)):
    x = pd.read_table(fileList[i], skiprows = 3, header = None)
    with open('%s\\csv_files\\%s.csv' %(cwd,fileList[i][0:35]), 'a') as f:
        x.to_csv(f, index = False)
        
        
#Creates new CSVs with the averages of the column data

filePath = '*.lwi' #used to find all files ending in .lwi

#lists all files in path ending in .lwi
fileList = (glob.glob(filePath))

for i in range(len(fileList)):
    df = pd.read_table(fileList[i], skiprows = 3, header = None)
    averages = pd.DataFrame(df.mean())
    averages.to_csv('%s\\averages\\%s.csv' %(cwd,fileList[i][0:35]), header = False, index = False)
    
