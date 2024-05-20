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
    
    





























































