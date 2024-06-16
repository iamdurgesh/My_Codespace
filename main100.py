# python hands on revision

#1.Escape Sequence charachters
"""print("100days start \n this \" video \" has a no of things to learn. ",78787, sep="-", end="009\n")"""

#2. Variable and datatypes
"""a = 122
b = True
c = "StringData"
d = None

print("The type of a = ", type(a))
print("The type of b = ", type(b))
print("The type of c = ", type(c))
print (a , c)""" 

#3. List and Tuples and dictionary
"""List1 = ["number", 132131, True, 31231, [312312]]
tuple = ("tuple1", "tuple2", "tuple3") #tuple is immutable unlike lists
dictionary = {"sagar":"Boy",  "sahil":"girl"}
print(List1, tuple, dictionary)"""

#4. Arithmetic operators
"""a = 15**2 # Exponential operator
b = 15%5  # Modulus operator
c = 15//2 # floor division
print(a,b,c)"""

#5. Python Typecasting
"""a = "2323"
b = 2121
print(int(a) + b)"""


#6. Input in Python
"""a = input("Enter your ID: ") 
b = input("Enter the ID PF your friend: ")
print("Id no's are confirmed as", int(a)," & ",  int(b))"""

#7. Strings
"""text = "he said there is something strange happening 'said by ally' ram"

#using for loop to prin all the characters in the word
for charachters in text:
    print(charachters)"""
    
#8. string slicing [0:n]
"""names = "ally, Sally, Rally"
print(names[7:11], len(names))
fruit = "apple"
print(fruit[-3:-1])  #length of the ruit is taken by default so (5-3 = 2, 5-1 = 4) = (2:4)"""

#9. Immutability in strings
"""a = "Connemara"
print(len(a))
print(a.upper())   #string are immutable, so everytime when upper or lower called, a new string is made
print(a.lower())
print(a.replace("Connemara","Glenfeddich"))
phrase = "journey to the mysterious island to morroco"
print(phrase.capitalize())
print(phrase.center(20))
print(phrase.count("to"))    #counts the no of occurences
print(phrase.endswith("morroco"))
print(phrase.find("topc"))       # finds and returns the index of the result,, otherwise returns -1
print(phrase.isprintable())         # returns false for non printable charachters, like \n, carriagge return
print(phrase.startswith("jou"))
print(phrase.swapcase())"""

# 10. If-else statements with nested statements
"""form = int(input("Welcome to the driving school, press'1' for weiter & '2' for cancel: "))
if(form == 1):
    a = int(input("Enter your age: "))
    print("Your age is ", a)
    if(a<=18):
        print("Entry is not allowed")
    elif(a>100):
        print("Too Old to enter")
    else:
        print("Welcome to the world of pleasure")
        q2 = str(input("Enter your full name: "))
        print("Your name is ", q2)
else:
    print("Thanks for coming to the school board")"""
    
# Exercise Good MORNING
"""import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
time = int(time.strftime('%H'))
print(time)
if (time>6 and time<12):
    print("Good Morning Pal")
elif(time>12 and time<18):
    print("Good Afternoon Buddy")
elif(time>18 and time<20):
    print("Good Evening Boiiii")
else:
    print("Goooood Night")"""

#11. MatchCase statements
"""x= int(input("Enter the value of x: "))
match x: 
    case 0:
      print("x is zero")
    case 4:
      print("case is 4")

    case _ if x!=90:
       print(x, "is not 90")
    case _ if x!=80:
      print(x, "is not 80")
    case _:
      print(x)"""
      
#12. For Loop ---------------

"""b = [1,2,3,4,5]
for a in b:
    print(a)"""

"""colors = ["red", "blue", "green", "orange", "saffron", "biege"]
for color in colors:
    print("Selected color is: ", color)
    for i in color:
        print(i)"""
        
"""for k in range(20):
    print(k+1)"""

"""for k in range(1,100,2):   #printing all odd numbers using a step in the argument
    print(k)"""

#13. While LOOP ----------------- THE LOOP KEEPS EXECUTING UNTIL THE CONDITION IS TRUE
#a. 
"""count = 5
while(count>1):
    print(count)
    count -= 1
else:
    print("while loop is stopped now")"""
    
#b.
"""i = int(input("Enter the number: "))

while(i<40):
    i = int(input("Enter the number: "))
    print(i)
else:
    print("The loop is over")"""
    
#14. Do-while Loop --------------- it executes at first and then if the condition is satisfied, then iterated again
#Emmulating do while loop in python, as it is not directly available in python 

"""i = 0
while True:
    print(i)
    i = i+1
    if(i/100 == 1):
     break
print("i am out of the loop")"""
 
#15. Break and continue

"""for i in range(15):
    if(i >10):
        continue
    print("5 X ", i, " = ", 5*i)
    
    
print("Breakin out of the loop")"""


# 16. functions in python ------------------- you

"""def calculateGmean(a,b):
    mean = (a*b)/(a+b)    
    print(mean)
    

def isGreater(a,b):    
    if (a>b):
        print("First no is greater")
    else:
        print("Second no is greater or equal")
        
def isLesser(a,b):
    pass

a = 10
b = 2
calculateGmean(a,b)
isGreater(a,b)
"""


# 17. Functions as an arggument
"""def average(a,b):   #a & b are required arguments
    print("The average is ", (a+b)/2)

average(3,6)"""

# variable length argument
##a. list
"""def average(*numbers):    #  *numbers: * used to define as tuple
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is:", sum/len(numbers))
    return sum/len(numbers)

call = average(5, 6, 7,8)    # to call the function
print(call)"""


#b. dictionary
"""def name(**name):
    print(type(name))
    print("Hello, ", name["fname"], name["mname"], name["lname"])
    
name(fname="oyyyy", lname="oyo", mname="oyeeeee")"""

#18. list in python (To store multiple inputs in one name)

"""marks = [2,4,6,8, "string", True]
print(type(marks[3]), marks)

marks.append(45)
print(marks[1:-1])
print(marks[1:7:2])    #will jump the index in the third value
print(marks[:4])"""


# ---------List comprehension (Generating list on the fly)
"""lst = [i*i for i in range(10) if i%2==0]
print(lst)"""

# List methods for manipulation

#l = [11,21,31,14,5,11]

# l.append(23,)
# l.insert(0, "string")
# l.reverse()
# print(l.count(11))

"""m = ["a", "b", "c"]
l.extend(m)                 # the list l is also changed here, 
print(l)"""

"""k = l + m                   # here the original list is not changed
print(k, l)"""


# copy method in list
"""m = l      #here m is a reference for l, so if m changes, then the value of l also changes, so there is no additional copy created of the list as m
m[0] = 1000
print(l)"""

"""m = l.copy()
m[3] = ["insert 11"]                                                  # here a new copy will be made using the copy function
print(l, m)"""


# 19. ------------------------ Tuple-----------(Non changeable) (the only way to add a new item in tuple is by converting it to list and then convert back to tuple)

# a
"""tup = (1,4,66,790,"string", False, None)                           # append or insert does not work on tuple, the size is always fix                                     
lst = [1,2]
# tup.append(12)                                                      # will not work
lst.append(12)
print(type(tup), tup, lst)
print(tup[-3])
def testvalue(a):
    if a in tup:
     print("value", a, "is present")
     return a 
 
testvalue(66)

tup1 = tup[:5]
print(tup1, tup)"""


# b.
"""tupl1 = (0,1,2,3,4,5,6,7,8,9,1,2,3,3,2,4,1,5,7,8,5,3,2)
res = tupl1
print(len(res))"""


# changing tuple
"""countries = ("india", "china", "italy", "England", "Germany", "France")

lst = list(countries)
lst.append("USA")
lst.remove("china")
lst.pop(2)
lst[3] = "Hungary"
countries = tuple(lst)
print(type(countries))
print(type(lst))"""


# 20. -------------  f-strings    (Solving string formatting issue)  making interpolation easier

"""letter = "Hey Buddy!, my name is {1} and i am from {0}"
country = "Russia"
name = "Ladislav"                                       #There is a prblem of interchanging even by giving index, we can forget which index refers to which value
print(letter.format(name, country))
#Solution
print(f"Hey Buddy!, my name is {name} and i am from {country}")  # f"{}" fstring make it easier
#to retain curly barckets as well add double curly brackets
print(f"Hey Buddy!, my name is {{name}} and i am from {{country}}")"""

# b.
"""offer = "offer is 10mil Pounds cash"
value = int(49.19)
print(f"the {offer}, Sofort in the bank account. But the account balance is {value:.2f}")   # :.2f to get the floor 2 decimal values

# making int to string as a type
print(type(f"{3*66}"),f"{3*66}" )"""

#20. Docstrings   ( used To document the code, can be accessed by __doc__ , it is not similar to comments) 



# def square(n):
#     """Takes a number n, returns the square of the number"""     # defined only after the next line in the function defination
#     print(n**2)

# square(5)
# print(square.__doc__)




# PEP 8  = PYTHON ENHANCEMENT PROPOSALS, DOCUMENTS FOR BETTER USABILITY AND CODE IMPROVISATION IN PTHON
# TRY WRITING "import this" in console after calling python3, you will see the zen of python

#21. *** Recursion in pthon 

# a. Factorial calculation   (n! = n*(n-1)!)

"""def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num-1))

#driver code
print(factorial(1))

# b. Fibonacci Series (f(n) = f(n-1)+f(n-2))

def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1 or n==2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# driver code
print(fibonacci(6))"""


#22. ------ Sets ------- (Unordered data of items, which cannot be replaced as the index is not static, also no repitition of duplicate value)
 # When you don't need repition in the list items, we use set to prevent this

"""s1={}                               # Empty Dictionary
s2 = set()                          # Empty Set
print(type(s2))"""

"""set1 = {1,22,333,4444,55555}
set2 = {666666, 7777777, 88888888, 22}
# set3 = set1.union(set2)
# set1.update(set2)
# set1.intersection(set2)                         
set = set1.symmetric_difference(set2)                   # gives all the values which are not common, and creates a new set
set1.add(999999999)
set1.remove(333)
set2.clear()
print(set2)
# print(set)
# print(set1)
print(f"the values update in set 1 are ",set1)
# print(len(set3))"""

# 23. -------- Dictionary  (Fast accessibility of the items collection) ordered after v3.7

"""dct = {
    104 : "Neha",
    105 : "Sassy",
    106  : "Ravi",
    
}
# print(dct[105])             # throws the error of not found
# print(dct.get('Ne'))        # throw none if not found
print(dct.keys())
print(dct.values())

for key in dct.keys():
    print(dct[key])                     # gives the value of the key
    print(f"the value of the key {key} are {dct[key]}")"""
    
# for key value items
"""dct = {
    104 : "Neha",
    105 : "Sassy",
    106  : "Ravi",
    
}
print(dct.items())"""

# Performing operations in the dictionary
#a. update
"""EP1 = {1:"a",
       2:"b",
       3:"c"}

EP2 = {
    3:"c",
    4:"d",
    5:"e",
    6:"f",
}
# EP1.clear()
# EP1.update(EP2)
# EP1.popitem()               #POPS THE LAST ITEM
# EP1.pop(2)                    # pops the particular value
del EP2[4]
print(EP2)
print(EP1)"""


# 24. ----------- Using else with For loop
"""for i in range(5):
    print(i*5)
else:
    print("Sorry, out of the loop now") """
    
"""for i in range(8):
    print(i)
    # if i==4:                  # Remember here the else is not called as the loop breaks before the completion of the loop
        # break
    
else:
    print("Out of the loop")"""
    
# 25. Exception Handling/ Error handling in python using (try-except)   **very important


"""a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(f"The error occured as the user input was {type(a)}")

    
    print("The value is not a number")   """
    
"""try:
    num = int(input("Enter the number: "))
    a = [6,3]
    print(a[num])                                   # Handling multiple errors
except ValueError:
    print("Number is not an integer")
    
except IndexError:
    print("Index Error happend")
    
except SyntaxError:
    print("Invalid syntax")"""
    
# 26. ***Using Finally in error Handling  (it will always execute even after returning inside try or except)

"""try:
    l = [1,33,55,67]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error has occured")

finally:
    print("this will always execute")
"""
"""def func():     # When even called in a function, finally will always execute even if except or try have returnd the value before
    try:                                
        l = [1,33,55,67]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error has occured")
        return 0

    finally:
         print("this will always execute")

x = func()
print(x)"""

# 26. Raising custom errors 

"""a = int(input("Entera any value between 1 and 100: "))

if (a<1 or a>100):
    raise ValueError("Bc value limit mein daal na")

print(a)"""

# an object which should only accept "quit"as an input
"""a = str(input("Enter the correct string: "))

if (a != "quit"):
    raise ValueError("Incorrect string typed")

print(f"the value entered is matching with {a}")"""
    
# 27: Exercise (Secret Code Language)







# 28. Shorthand for if-else

"""a = 100000
b = 10000
print("A") if a > b else print("Gleichnummern") if a== b else print("B") #Shorthand"""

# zb.2
"""c = 9 if a > b else 0
print(c)"""

# zb:3
"""result = value_if_true if condition else value_if__false
# is equivalent to 
if condition:
    result = value_if_true
else:
    result = value_if__false"""
    
# 29: Enumerate function:      used to loop over a sequence

"""marks = [22,33,44,23,75,55,7,99]
index = 0
for mark in marks:
    print(mark)
    if(index == 4):
        print("index without enumerate")
    index +=1"""
    
    #1 Solution
"""marks = [22,33,44,23,75,55,7,99]

for index, mark in enumerate(marks):   # returns a tuple
    print(mark)
    if(index == 4):
        print("index without enumerate")"""


    #2 solution
"""colors = ["black", "green", "blue", "orange"]

for index, color in enumerate(colors, start = 1):
    print(colors)
    if(index == 2):
        print("Mango juice")"""


#30 

# 31  Learn how to import

# import testfunc;

# testfunc.welcome()

# # OS module in python (used to perform actions, or automate file actions)

# import os
# os.mkdir("data")

# # if(not os.path.exists("data")):
# #     os.mkdir("data")
# for i in range(0,100):
#     # os.mkdir(f"data/testFolder{i+1}")
#     os.rename(f"data/testFolder{i+1}", f"data/folderRenamed {i+1}")     # rename method
#     os.remove(f"data/folderRenamed {i+1}")     # remove method

# # to remove a file
# # os.remove("test.py")

#31 # import testfunc;

# testfunc.welcome()

# # OS module in python (used to perform actions, or automate file actions)

"""import os
os.mkdir("data")

# if(not os.path.exists("data")):
#     os.mkdir("data")
for i in range(0,100):
    # os.mkdir(f"data/testFolder{i+1}")
    os.rename(f"data/testFolder{i+1}", f"data/folderRenamed {i+1}")     # rename method
    os.remove(f"data/folderRenamed {i+1}")     # remove method

# to remove a file
# os.remove("test.py")"""


#32  Local vs Global Variables
"""x = 10 # global variable

def a_function():
    global x        #using global inside leads to unexpected behaviour and harder to debug
    x = 100
    y = 5
    print(y)
    
a_function()
print(x) """



# 33 File IO / File handling
"""f = open('myFile2.txt', 'w')  # to write in a file use this, also if not exists already it will create a new file
f = open('test_file.txt', 'x')   # to create a new file
f = open('myFile.txt', 'w')   # while using write, it will write on the file, it will remove all the preivous data if the file name is same
f = open('myFile.txt', 'a')   # while using write, it will append on the file, it will not remove all the preivous data if the file name is same
print(f)
text = f.write('Heya, now the append should add the this text in the file')
f.close()
print(text)

with open('file_a.txt', 'w') as f :
    f.write(f"this file is generated using a code snippet where we don't have to close it \n")"""
    
# 34 read(), readlines(), writelines() and other methods
# 1A. also update the file_a.txt to the marks values 
"""f = open('file_a.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
     break
    m1 = int(line.split(",")[0])
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f" Marks of student {i} in maths are: {m1 *2}")
    print(f" Marks of student {i} in maths are: {m2 *2}")
    print(f" Marks of student {i} in maths are: {m3 *2}")

    print(type(line))"""
    
# B.
"""f = open('file_a.txt','w')
lines = ['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()"""


#35 Seek(), tell(), and other functions
#35 a.
"""#used to
with open('myFile.txt', 'r') as f:
    print(type(f))
    f.seek(10)        # to move to the 10th byte in the file

    print(f.tell())   #To see the current position
    data = f.read(5)        #read the next 5 BYTES
    print(data)"""

#35 b.    
"""with open('sample_file.txt', 'w') as f:
    f.write('Hello World 51!!')
    f.truncate(10)      # To trucate the file to a specific size    

with open('sample_file.txt', 'r') as f:
    print(f.read())"""
    
#36 Lambda functions
"""# def double(x):
#     return x*2

double = lambda x: x*2
print(double(6))
cube = lambda x: x*x*x
print(cube(3))
avg = lambda x,y,z: (x+y+z)/3
print(avg(3,5,7))
m2cm = lambda x: x*100
print(f"value of meter to cm is {m2cm(4)} centimeters")

def useCase(fx, value):
    return 100 + fx(value)
# It is mostly used when want to pass a function as an argument
print(useCase(cube, 4))"""



#37 Map, Filter, and Reduce in Python
#a. Map
"""def cube(x):
    return x*x*x
print(cube(2))
l = [1,2,3,4,5]
newl = []
# for item in l:
#     newl.append(cube(item))
# newl = list(map(cube,l))  #instead of using a for loop we can use a map function and also a lambda instead of a cube function
newl = list(map(lambda x:x*x*x, l))
print(newl)


#b. ----- Filter
# def filter_function(a):
#     return a>2
# newnewl = list(filter(filter_function, l))
newnewl = list(filter(lambda x:x>2,l))   # similarly here also we use a lambda function instead of the filter_function defined.
print(newnewl)"""

#c. Reduce (Ex: Reducing the sum of numbers)
"""from functools import reduce
numbers = [5,5,5,5,10,20,30]
number1 = [1,2,3,4,5]
#calculating using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
product = reduce(lambda x, y: x*y, number1)

print(product)
print(sum)"""

#38 "is" vs "==" 
# 'is' compares the exact location of object in the memory, while '==' compares the value
"""a = 100     # Constant are saved as a single object, so python will store both a & b in a single memory location 
b = 100
c = [12,23]     # List are mutable, so they will be stored at individual memory location
d = [12,23]
e = ("iphone","macbook")  #immutable tupple, so must be true
f = ("iphone", "macbook")
print(a is b)
print(a == b)
print(c is d)
print(c == d)
print(e is f)
print(e == f)"""

#39 Exercise 5 Snake Water Gun
# 'is' compares the exact location of object in the memory, while '==' compares the value

#40 OOPS in Python    
# It consistes of classes(blueprint or template for creating objects) and objects(instance of a class, has its own data and methods) 
#   
#41 Classes and Objects
"""class Person:
    name = "Henrick"
    occupation = "Developer"
    networth = 10
    def info(self):   #try to use "self" when defining a function in a class
        print(f"{self.name} is a {self.occupation}")
        

# Here we can use the class multiple times 
a = Person()
a.info()
b = Person()
b.name = "Ronnie"
b.occupation = "Designer"
b.info()

c = Person()
c.name = "Mascha"
c.occupation = "Archeologist"
c.networth = str("100 Millions")
print(f"{c.name} is a {c.occupation} and has {c.networth}")"""

#42 Constructors in python
"""# it is a special method in a class to initialize an object of a class, gets called automatically when an object is created in a class, it returns none

class Person:
    # def __init__(self):           # Default Constructor
    #     print("Hey a constructor is initialised")
    
    def __init__(self, naam, kaam): # Parameterized Constructor
        print("Hey Your constructor is passed")
        self.name = naam  
        self.occupation = kaam   
        

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Ronnie", "Artist")
b = Person("Rishi", "Designer")
# a.name = "Disha"
# a.occupation = "Wholeseller"
a.info()
b.info()"""

#43 Decorators in Python
#They are used to modify functions(decorator fuction takes another function as an argument(nested function))

"""def greet(fx):
    def mfx():
       print("Greet function is called") 
       fx()
       print("Thanks for using this greet function")
    return mfx

# def Hello():                          
#     print("Hello Worldie")
    
# greet(Hello)()        # here if we don't use the decorator, we call the function, less readability

@greet
def Hello():
    print("Greeting for the World")

Hello()                 # Better Readability"""
    
# b
"""def decorator(fx):           
    def mfx(*args, **kwargs):
        print("Greet function is called") 
        fx(*args, **kwargs)
        print("Thanks for using this greet function")
    return mfx

def add(a, b):
    print(a+b)
    
@decorator
def Hello():
    print("Greeting for the World")

Hello()   
decorator(add)(1,4)"""

# Logging Module
"""import logging
def log_function__call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args = {args}, kwargs = {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned{result}")
        return result
    return decorated

@log_function__call
def my_function(a,b):
    return a + b
    """
    
#44 Getters and Setters in python
"""class MyClass:
    def __init__(self, value):
        self._value = value
        
    def show(self):
        print(f"Value is {self._value}")
        
    # @property       #Works as a getter, looks like a property, but is a method(encapsulation)
    # def value(self):
    #     return 10* self._value
    
    @property     
    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10
    
obj = MyClass(10)
obj.ten_value = 20
print(obj._value)
print(obj.ten_value)
obj.show()"""

#45 Inheritance in Python

"""import math
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
         print(f"The name of the employee: Id = {self.id} is {self.name}")
         
class Programmer(Employee):      # it will inherit all the properties of class Employee
    def showLanguage(self):
        print("The default language is Python")
        
        
e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Raamu", 123)
e2.showDetails()
e2.showLanguage()"""

#46 Access Modifiers in Python
"""# How Public private and protected  work in python, to limit the access. All self modifiers are public by default
#There is no primary concept of public private and protected in python
class Employee:
    def __init__(self):
        self.__name = "Harry" # "__" double underscore before the modiefier makes it private

a = Employee()
# print(a.__name)               #Cannot be acessed directly
print(a._Employee__name)        #can be accessed indirectly  using name mangling
print(dir(Employee))


# Name Mangling : we use it to protect class-private and subclass-private attributes from being overwritten by subclasses

#EX-2
class Student:
    def __init__(self):
        self._name = "Donnie"

    def _funName(self):
        return "CodeWithDonnie"
class Subject(Student):  #inherited class
    def sub(self):
        return "Mathematik"
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))  # to check the _varName in the directory
# calling by object of student class
print(obj._name)
print(obj._funName())   # Single underscore is mostly for naming convention
# Calling by object of the subject class

print(obj1._name)
print(obj1._funName())
print(obj1.sub())"""

#47 Exercise 6 Library Management System
# Write a library class with no_of_books and books  as two instance variables, write a program to create 

#48 Static Methods in Python
#These methods neither belong to a instance nor class

"""class Math:
    def __init__(self, num):
        self.num = num
        
    def addtoNum(self, n):
        self.num = self.num + n
    
    @staticmethod
    def add(a, b):
        return a + b   
    
result = Math.add(1, 2)
print(result)

a = Math(5)
print(a.num)
a.addtoNum(76)
print(a.num)

print(Math.add(77,2))"""

#49 Instance Variables vs Class Variables
"""# Understand each and every step..
class Employee:
    companyName ="Apple"            # Class Variable(same for the whole class)
    noOfEmployees = 10
    def __init__(self, name):
        self.name = name
        self.raise_amount = 5000
        Employee.noOfEmployees +=5
        
    def showDetails(self):
        print(f"The Name of the Employee is {self.name}, and the raise amount is {self.raise_amount} and he works in {self.companyName}, whose company size is {self.noOfEmployees}")
        
        

emp1 = Employee("Ronnie")
Employee.showDetails(emp1)           #INSTEAD OF CALLING LIKE THIS
# emp1.showDetails()                  # We can do this
emp1.companyName = "Alstom"
print(emp1.companyName)             # if there is an instance variable present, then it will use it, otherwise the class variable will be shown
emp1.showDetails()   

emp2 = Employee("Amanda")      
emp2.raise_amount = 0.3
emp2.showDetails()"""


#Exercise 7 
#Write a program to clear the clutter inside a folder on your computer. You should use the os module to rename all te png images from 1.png,, all the way till n.png where n is the numner of png files in that folder. Do the same for other file formats.For Example:


#50 Class Methods

"""class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company name is {self.company}")
    
    @classmethod   #print once before and after commenting this
    #Using the above method the 1st argument in "cls" below will be a taken as a class instead of an instance
    def changeCompany(cls, newCompany):
        cls.company = newCompany
        
    
    
e1 = Employee()
e1.name = "Raamu"
e1.company = "Panasonic"
print((e1.company))
e1.show()
e1.changeCompany("TATA")
e1.show()
print(Employee.company)         # The result was Apple, not TATA, because the class was not updated without using the classDecorator
"""


#51 Class Methods as Alternative Constructors

# Example 1
"""class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("_")[0],int(string.split("_")[1]))  #Using class method as an alternative constructor
        
e1 = Employee("Jamun", 2100)     #Instance
print(e1.name, e1.salary)

string = "Harry_12000"
# e2 = Employee(a.split("-")[0],a.split("-")[1]) #Instead of using this for each instance, we can make a classmethod, return the string with the parameters
# print(e2.name)
# print(e2.salary)


e2 = Employee.fromstr(string)           # we use the the class as a constructor here
print(e2.name)
print(e2.salary)"""

#-----Example2
"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def fromstring(cls, string):
        name, age = string.split(", ")
        return cls(name, int(age))

person = Person.fromstring("Namanda, 69")
print(person.name, person.age)
    """
    
#52 dir, _dict_ and help method in python


#a. dir method:  They are used for object intro-spection, to check how classes resolve various functions and executes code

"""x = [1,2,3,4]
y = (23,15,55)
print(dir(x))
print(len(dir(x)))
print(len(dir(y)))

print(x.__init__)
# print(x.__dict__)

#b. __dict method

class Person:
    def __init__(self, team, color, points):
        self.team = team
        self.color = color
        self.points = 12
        
p = Person("Bayern", "Red", 23)
print(p.__dict__)

#c help method : it will give all the details for an object, including its attributes and methods
print(help(Person))"""
        
#53 Super Keyword in Python 

# Used to call/refer parent methods/class from child class
"""class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

        
class ChildClass(ParentClass):
    def parent_method(self):
        print("Parent Method in child class")
        super().parent_method()     # This will also call the parent method from the parent class
    def child_method(self):
        print("This is a child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()"""

#Ex.2
"""class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
# class Programmer:
#     def __init__(self, name, id, lang):
#         self.name = name
#         self.id = id
#         self.lang = lang      

# Use superkeyword instead
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
        
a1 = Employee("Tony", 443)
a2 = Programmer("Ronnie", 576, "typescript")
print(a1.name)
print(a2.name)
print(a2.id)
print(a2.lang)"""

#54 Magic Dunder Method in Python (special methods, we can define in our classes, they give powerful way to manipulate objects with their behaviour)

"""class Employee:
    def __init__(self,name):
        self.name = name    
        
    def __len__(self):
        i = 0
        for c in self.name:
            i+=1
        return i

    def __str__(self):
        return f"This name of the employee is {self.name} str"

    def __repr__(self):
        return f"The name of the employee is {self.name} repr"
    
    def __call__(self):
        a = str(input("What is your name: "))
        return print(f"The name is saved as {a} ")
        
    
e = Employee("Donald")
print(e)
print(str(e))
print(repr(e))
e()"""
# print(e.name)
# print(len(e))

# Further methods are also used for operator overloading like __mul__ ,__add__

#55 Method Overriding in Python :
# to redefine a parent class method according to the child class

"""class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x* self.y

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14 * self.radius * self.radius
# Now instead we can also override this method using a super:

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)
        
    def area(self):
        return 3.14 * super().area()
    
rec = Shape(2,4)
print(rec.area())

a = Circle(100)
print(a.area())"""

#56 Operator Overloading in Python
"""class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    # def __add__(self, x):
    #     return f"{self.i + x.i}i + {self.j + x.j}j + {self.k+x.k}k"
    # TO Change the type from str to vector
    def __add__(self, x):
         return Vector(self.i + x.i,self.j + x.j, self.k+x.k)
    
v1 = Vector(3, 6, 3)
v2 = Vector(3, 3, 3)
print(v1)
print(v2)
print(v1+v2)
print(type(v1 + v1))"""

#57 Single Inheritance in Python
# Here the class inherits properties from a single parent class
#syntax: class childClass(ParentClass):

"""class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print(f"Sound made by the animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species = "Dog")
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!!!")

# d = Dog("Tony", "Bulldog")
# d.make_sound()
# a = Animal("Bruno", "DobberMan")
# a.make_sound()

#Ex.2
class Cat(Animal):
    def __init__(self, name, owner):
        Animal.__init__(self, name, species)
        self.owner = owner
        super().make_sound()
        
c = Cat("Pussy", "Johnny")
c.makesound()"""
        
#58 Multiple Inheritance in Python 

class Employee:
    def __init__(self, name):
        self.name = name
        
class Dancer:
    def __init__(self, dance):
        

class DancerEmployee(Employee, Dancer):
    pass

#59 Multilevel Inheritance in Python:

#60 Hybrid and Hierarchical Inheritance in Python:

#61 Time Module in Python 

#62 Creating a commandLine utility in Python:























































