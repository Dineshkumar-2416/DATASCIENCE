# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:01:24 2024

@author: mdine
"""
'''
no _ - 
_ - notionnally privaate y? tells  user that  notto  chnage  data (it ll  still  change)
__ - strictly private - observation - can access outssidde thee class. 


HW : __ inside class...access outside the cls using clsmethod 
__ outside cls ...do somefn on it. is both __ same?

'''

'''CLASS_COMPLEX'''

# class comp():
#     def __init__(self, r,i):
#         self.real = r
#         self.img = i
        
#     def __add__(self, other):
#         return c1 + c2

# c1 =comp(5,6)
# c2 = comp(7,8)
# comp.add(c1,c2)
        
class Complex:
    def __init__(self, r=0, im=0):
        self._real = r
        self._imag = im
        print(self)
        
    #Addition of two complex numbers using a method
    def add_comp(self, other):
        c = Complex()
        c._real = self._real + other._real
        c._imag = self._imag + other._imag
        return c
    
    #Addition of two complex numbers using operator overloading
    def __add__(self, other):
        c = Complex()
        c._real = self._real + other._real
        c._imag = self._imag + other._imag
        return c
    
    def __sub__(self, other):
        c = Complex()
        c._real = self._real - other._real
        c._imag = self._imag -  other._imag
        return c
    
    def print_comp(self):
        print('real = ', self._real, 'imag = ', self._imag)
    
c1 = Complex(4.5, 5.45)
c2 = Complex(3.5, 8.45)
# c3 = Complex(4,2)
# c3.print_comp()
c3 = c1.add_comp(c2)
c1.print_comp()
c2.print_comp()
c3.print_comp()

c3 = c1 - c2  #Using the symbol for addition
c3.print_comp()

c3 = c1 + c2  #Using the symbol for addition
c3.print_comp()


'''HW: OPERATOR OVERLOADING , IS there FUNCTION OVERLOADING in python?'''



'''L11 - CLASS_CONTAINER_AND_INHERITANCE'''


class Base:
    def __init__(self, name, roll, marks):
        self.name = name
        self._roll = roll
        self.__marks = marks
    
    def samename(self):
        print('Inside same name of base')
        
    def printbase(self):
        print(self.name, self._roll, self.__marks)
        
class Derived(Base):
    def __init__(self, name, roll, marks, name1, roll1, marks1):
        super().__init__(name, roll, marks)
        self.name1 = name1
        self._roll1 = roll1
        self.__marks1 = marks1
        print('Inside init', id(self.__marks1))
        # changing the details of the base
        self.name = 'Newname'
        self._roll = 4356
        self.__marks = 89
        
    def samename(self):
        print('Inside same name of derived')
        
    def printderived(self):
        super().printbase()
        print(self.name1, self._roll1, self.__marks1)
        print(self.name, self._roll, self.__marks)
        
d1 = Derived('Ram', 1234, 85, 'Raman', 4356, 76)
d1.printderived()
d1.name1 = 'Ramamoorthy'
d1._roll1 = 8890
d1.__marks1 = 10  #Cannot change this
print('outside init', id(d1.__marks1))

d1.name = 'Siva'
d1._roll = 34566
d1.__marks = 23
d1.printderived()

d1.samename()

print('Just printing')
print(d1.name1, d1._roll1, d1.__marks1)
print(d1.name, d1._roll, d1.__marks)   





























