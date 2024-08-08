# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:04:49 2024

@author: mdine
"""

# Multi-level inheritance
class Base:
    def display_base(self):
        print("Base class method")


class Derived1(Base):
    def display_derived1(self):
        print("Derived1 class method")


class Derived2(Derived1):
    def display_derived2(self):
        print("Derived2 class method")



obj = Derived2()
obj.display_base()    
obj.display_derived1()  
obj.display_derived2() 


#Multi-level inheritance

class Base:
    def __init__(self, name):
        self._name = name
        print('Inside base constructor')
          
    def printbase(self):
        print('Inside base print')
        print(self._name)
        
    def __del__(self):
        print('Inside the destructor of base')
    
class Derived1(Base):
    def __init__(self, name):
        super().__init__(name)
        print('Inside derived1 constructor')
    
    def printderived1(self):
        print('Inside derived1 print')
        print(self._name)
    
    def __del__(self):
        #super().__del__()
        print('Inside the destructor of Derived1')
        
class Derived2(Derived1):
    def __init__(self, name):
        super().__init__(name)
        print('Inside derived2 constructor')
    
    def printderived2(self):
        print('Inside derived2 print')
        #self.printderived1()
        #Derived2.printderived1(self)
        #super().printderived1()
        print(self._name)
        
    def __del__(self):
        #super().__del__()
        print('Inside the destructor of Derived2')
        
d2 = Derived2('Ram')
d2.printderived2()
d2.printderived1()
d2.printbase()

#d1 as object of derived one
d1 = Derived1('Raman')
#d1.printderived2() #cannot be done
d1.printbase()


# Multiple inheritance
class Base1:
    def display_base1(self):
        print("Base1 class method")


class Base2:
    def display_base2(self):
        print("Base2 class method")


class Derived(Base1, Base2):
    def display_derived(self):
        print("Derived class method")



obj2 = Derived()
obj2.display_base1()  
obj2.display_base2()  
obj2.display_derived()  


#Multiple inheritance

class Base1:
    def __init__(self, name):
        self.name = name
        print('Inside base1 constructor')
          
    def printbase1(self):
        print('Inside base1 print')
        print(self.name)
        
    def printdata(self):
        print('Inside base1 printdata')
        print(self.name)

    
class Base2:
    def __init__(self, roll):
        self.roll = roll
        print('Inside base2 constructor')
          
    def printbase2(self):
        print('Inside base2 print')
        print(self.roll)
        
    def printdata(self):
        print('Inside base2 printdata')
        print(self.roll)


class Derived(Base1, Base2):
    def __init__(self, name, roll):
        #super().__init__(name)
        Base1.__init__(self, name)
        Base2.__init__(self, roll)
        print('Inside derived1 constructor')
    
    def printderived1(self):
        print('Inside derived1 print')
        print(self.name, self.roll)
        
    def printdata(self):
        #super().printdata() #Access Base1 printdata
        print('Inside derived printdata')
        print(self.name, self.roll)

d1 = Derived('Ram', 12345)
d1.printderived1()
d1.printbase2()
d1.printbase1()
d1.printdata()

'''To create GUI and front end , we use qt aand tk library'''
'''HW - containership'''
'''Abstract classrr andrr  what are they?'''
        

'''Dynamic creation of attributes'''
class Passbook:
  pass
p1 = Passbook( )
p1._name = 'Raman'
p1._number = 1234