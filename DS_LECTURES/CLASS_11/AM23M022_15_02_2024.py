# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 10:02:10 2024

@author: mdine
"""
def var_arg(*d):
    #su = 0
    for var in d:
        #su += var
        #print(su, var)
        print(var, type(var))
        
var_arg('passing two arguments', 1, 5)
var_arg('passing three arguments', 1, 5, 'Ram')

lst = [1,2,3]
var_arg(lst)



def kwvar_arg(**kw):
    
    for k,v in kw.items():
        print(k,v)
        
        
kwvar_arg(i = 10)
kwvar_arg(i = 10, j = 20.34)
kwvar_arg(i = 10, j = 20.34, k = 'Ram')

'''
Variable length positional arguments - number of args is not fixed
• Variable length keyword arguments - number of keyword args is not fixed
'''
# default argument

def TorF(cond = True):
    if cond == True:
        print('True')
    else:
        print('False')
        
TorF()
TorF(False)

def win(d=8):
    if d ==  8:
        print('Correct guess')
        
    else:
        print('Incorrect guess')
        
win(7)


# all arguments at once
# def args_all(*d, **dk, k=6):
#     for var in d,dk,k:
#         print(var, type(var))
        
# args_all(1,5,k=6)
def ex(p_arg1, p_arg2, k_arg1, k_arg2, cond= "thambi tea innu varala"):
    print("Positional arguments:", p_arg1, p_arg2)
    print("Keyword arguments:", k_arg1, k_arg2)
    print("default arguments:", cond)


# ex(10, 10000)

# ex(10, 1000, k_arg1="kavi")

ex(700, 75000, k_arg1="dinesh", k_arg2="valentine")

# Recursion function
def PrintNum(n): #Function definition
 PrintNum(n-1) #Recursive call to the same function 
PrintNum(2) #calling of the function - this is when the function gets called
# maximum recursion depth exceeded 

def PrintNum(n): #Function definition
 PrintNum(n-1) #Recursive call to the same function 
 return n-1
PrintNum(2)
# maximum recursion depth exceeded


def PrintNum(n):
    if n> 0:
        print(n)
        PrintNum(n-1)
PrintNum(2)

# Sum of n numbers using recursion
def sum(n):
    sum_total = 0
    if n>0:
        for i in range(n+1) :
         sum_total += i
    return sum_total
sum(5)

'''
CW: Do the factorial of any given value ’n’ using recursion 
HW: Series summation - odd factorial, even factorial, 
exp(x), sin(x), etc. using recursion 
HW: Find the sum of digits of a given integer
'''