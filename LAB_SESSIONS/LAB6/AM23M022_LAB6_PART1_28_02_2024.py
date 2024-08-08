# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:14:07 2024

@author: mdine
"""
'''
Design a class named Polygon that initializes with the length of a side. 
Then, derive a class named Square from the Polygon class. 
Utilize the side length defined in the Polygon class for the Square class. 
Within the Square class, implement a method called findArea() that calculates 
and returns the square's area based on its side length. 
Use __init__() for necessary initialization'''

class Polygon:
    def __init__(self, length):
        self.length = length
        
class Square(Polygon):
    def __init__(self, length):
        super().__init__(length)
        
    def findArea(self):
        
        
        return self.length ** 2

square = Square(7)
y = square.findArea()
print("Area of the square:", y ) 

'''
  2.  (a)  Create a class Father with attributes

 - father_name (string), father_age (int), father_talents (set of strings)

Create a class Mother with attributes:

- mother_name (string), mother_age (int), mother_talents (set of strings)

Create a class Child that inherits both father and mother with attributes: 

 - child_name (string), child_age (int), child_gender(string) 
 (b) Create a function getChildDetails() in Child 
 to input the details of the child, it’s father and mother 
 and printChildDetails() to print the details using    
 printChildDetails()
(c) Create an object of class Child and read the details
 by invoking getChildDetails() and display the details entered.
 (d) Create a function displayTalents() in class Child 
 that displays the talents of the child inherited from father and mother. A talent is inherited to a child if both
the parents possess it.'''


class Father:
    def __init__(self, father_name, father_age, father_talents):
        self.father_name = father_name
        self.father_age = father_age
        self.father_talents = father_talents

class Mother:
    def __init__(self, mother_name, mother_age, mother_talents):
        self.mother_name = mother_name
        self.mother_age = mother_age
        self.mother_talents = mother_talents

class Child(Father, Mother):
    def __init__(self, father_name, father_age, father_talents, mother_name, mother_age, mother_talents, child_name, child_age, child_gender):
        Father.__init__(self, father_name, father_age, father_talents)
        Mother.__init__(self, mother_name, mother_age, mother_talents)
        self.child_name = child_name
        self.child_age = child_age
        self.child_gender = child_gender

    def getChildDetails(self):
        self.child_name = input("Enter child's name: ")
        self.child_age = int(input("Enter child's age: "))
        self.child_gender = input("Enter child's gender: ")
        self.father_name = input("Enter father's name: ")
        self.father_age = int(input("Enter father's age: "))
        self.father_talents = set(input("Enter father's talents separated by comma: ").split(","))
        self.mother_name = input("Enter mother's name: ")
        self.mother_age = int(input("Enter mother's age: "))
        self.mother_talents = set(input("Enter mother's talents separated by comma: ").split(","))

    def printChildDetails(self):
        print("\nChild Details:")
        print("Name:", self.child_name)
        print("Age:", self.child_age)
        print("Gender:", self.child_gender)
        print("Father's Name:", self.father_name)
        print("Mother's Name:", self.mother_name)
        print("Father's Talents:", self.father_talents)
        print("Mother's Talents:", self.mother_talents)

    def displayTalents(self):
        common_talents = set(self.father_talents).intersection(set(self.mother_talents))
        print("\nCommon Talents Inherited by Child:")
        for talent in common_talents:
            print("-", talent)

# Creating an object of class Child and reading the details
child = Child("", 0, set(), "", 0, set(), "", 0, "")
child.getChildDetails()

# Displaying the details entered
child.printChildDetails()

# Displaying talents inherited by the child
child.displayTalents()


'''
3 . Text File Input Output

Create a .txt (text) file and use the pledge of India as 
the content of the text file.

Write a python program that reads this text file, 
processes it by counting the number of occurrences of each word in the file, 
and then writes the result back to a new text file. '''


def count_word_occurrences(text):
    word_count = {}
    words = text.split()
    for word in words:
        word = word.strip('.,?!;:"')
        word = word.lower()
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    # Read the content of the text file
    with open(r'E:\AM23M022_SEM2\DATASCIENCE_THEORY_AND_PRACTICE\Datascience_Submissions\LAB6\pledge.txt', 'r') as file:
        text = file.read()

    # Count occurrences of each word
    word_occurrences = count_word_occurrences(text)

    # Write the result to a new text file
    with open('word_occurrences.txt', 'w') as file:
        for word, count in word_occurrences.items():
            file.write(f"{word}: {count}\n")

    print("Word occurrences counted and saved to 'word_occurrences.txt'.")

if __name__ == "__main__":
    main()


'''
    4.  For a restaurant, create a parent class ‘Bill’ 
    which has the properties as 
    ‘Customer  name’, ‘Table Number’ and 
    ‘Order’ of which the name, order are strings and 
    table  number is a positive integer. 
    Define a method to extract the order details from the string and 
    return a 2-D array of ordered items & their number. 
Create a child class ‘ 'Restaurant Bill’ which has a property called 
‘Price list’ of the items and has a method to 
calculate the total bill amount by using the price list and order details. 
Also have a   method to print the complete bill for 
the customer including taxes and service charges.

     The strings will be of the following format:

     #Name: “Akshay” (Name of the customer)

     #Table Number: 7 (Table Number)

     #Order: “Item1x1,Item2x3,Item3x1,…” (ItemxNumber needed)

     #Price List: “Item1-100,Item2-70,Item3-250,...” (Item-Price)
   
     
   
    5. For the previous question( restaurant Bill) - 
    take name, table no, order details from a file, p
    rice list from another file and print the whole bill to the new file.
    
    
    
'''



class Bill:
    def __init__(self, customer_name, table_number, order):
        self.customer_name = customer_name
        self.table_number = table_number
        self.order = order

    def extract_order_details(self):
        order_details = []
        items = self.order.split(',')
        for item in items:
            name, quantity = item.split('x')
            order_details.append([name.strip(), int(quantity)])
        return order_details

class RestaurantBill(Bill):
    def __init__(self, customer_name, table_number, order, price_list):
        super().__init__(customer_name, table_number, order)
        self.price_list = self.parse_price_list(price_list)

    def parse_price_list(self, price_list):
        parsed_prices = {}
        items = price_list.split(',')
        for item in items:
            name, price = item.split('-')
            parsed_prices[name.strip()] = float(price)
        return parsed_prices

    def calculate_total_bill(self):
        order_details = self.extract_order_details()
        total_bill = 0
        for item, quantity in order_details:
            if item in self.price_list:
                total_bill += self.price_list[item] * quantity
            else:
                print(f"Item '{item}' not found in the price list.")
        return total_bill

    def print_complete_bill(self, output_file):
        total_bill = self.calculate_total_bill()
        tax = 0.1 * total_bill  # Assuming 10% tax
        service_charge = 0.05 * total_bill  # Assuming 5% service charge
        grand_total = total_bill + tax + service_charge

        with open(output_file, 'w') as file:
            file.write("---------- Bill ----------\n")
            file.write(f"Customer Name: {self.customer_name}\n")
            file.write(f"Table Number: {self.table_number}\n")
            file.write("Ordered Items:\n")
            order_details = self.extract_order_details()
            for item, quantity in order_details:
                file.write(f"{item}: {quantity}\n")
            file.write(f"Total Bill: ${total_bill}\n")
            file.write(f"Tax (10%): ${tax}\n")
            file.write(f"Service Charge (5%): ${service_charge}\n")
            file.write(f"Grand Total: ${grand_total}\n")
        print(f"Complete bill has been printed to '{output_file}'.")

# Example usage:
order = "Item1x1,Item2x3,Item3x1"
price_list = "Item1-100,Item2-70,Item3-250"
bill = RestaurantBill("Akshay", 7, order, price_list)
bill.print_complete_bill('bill.txt')



'''----------------------------------------------------'''
# Read order details from file
with open('order_details.txt', 'r') as file:
    order_lines = file.readlines()

order_info = {}
for line in order_lines:
    key, value = line.strip().split(': ')
    order_info[key.strip()] = value.strip()

# Read price list from file
with open('price_list.txt', 'r') as file:
    price_list = file.read()

# Create bill object and print complete bill to new file
bill = RestaurantBill(order_info['Name'], int(order_info['Table Number']), order_info['Order'], price_list)
bill.print_complete_bill('complete_bill.txt')
