# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 09:13:25 2024

@author: mdine
"""
'''  .stl - 3d file format'''
'''Open the file'''


msg = 'DINESH KUMAR M'
msga = 234
f = open('messages.txt', 'w') #Opens a file for writing
f.write(msg) #Writes a new string 
f.write(str(msga))
# f.close() #Closes the opened file
f = open('messages.txt', 'r')
data = f.read() #Reads ALL lines into data
print(data)

'''file working directory '''
import os

import shutil

print(os.name)
print(os.getcwd())
print(os.listdir('.'))
print(os.listdir('..'))
if os.path.exists('TestDir'):
    print('TestDir exists')
else:
    os.mkdir('TestDir')
    
os.chdir('TestDir')
print(os.getcwd())

import csv

f = open('test_csv1.txt' , 'r')
data = f.read() #Reads ALL lines into data
print(data)

import csv

with open('test_csv1.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Header names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and handles {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    
 


'''HW - JSON - JAVA SCRIPT OBJECT NOTATION,  diff  b/w json and dict'''