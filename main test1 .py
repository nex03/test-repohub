# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# I start here

print("1")  # prints the number
print("2")
print("3")
print("4")

i = 1
while i <= 1_0:
    print(i * "hi")
    i = i + 1

namnam = ["misha", "Anna", "leo", "arvid"]  # this is a list of objects with variable namnam
namnam[-2] = "leos"  # changes to leos instead of leo, -2 is second from the back in the variable namnam!
print(namnam)  # this prints variable namnam
print(namnam[0:3])  # prints 0,1 and 2 objects

# list methods

numbers = [1, 2, 3, 4, 5]  # declared variable numbers with these 5 objects
numbers.append(6)  # have chosen method append to add "6" to the variable numbers.
numbers.insert(1, -2)  # do put in only two numbers, inserts the second value/object/ in front of the index/placement/  of the first
numbers.remove(5)  # removes object with value 5
numbers.clear()  # clears all items in the list
print(numbers)  # prints numbers
print(
    1 in numbers)  # bolean expression (search). this asks if 1 is in the variable numbers. it gives false because we have cleared all the objects in the numbers.
print(
    len(numbers))  # this will tell us how many objects there are in the variable numbers. here it will be zero again because we cleared the variable with methos ".clear. "len" (length) in a build in function like "print and they both are purple.

# loops

numbersvar = [1, 2, 3, 4, 5]  # skapa variabel med objekten 1-5. han säger: declair a list of numbers
for nyvar in numbersvar:  # this is a "for-loop (loop variable nyvar) that writes items vertikalt - on each length
    print(nyvar)

i = 0  # declair variable outside of our while loop
while i < len(
        numbersvar):  # this is a "while-loop.its more cumbersome that for-loop. as long as i is less than the amount of objects in variable numbersvar...
    print(numbersvar[i])  # print values of i/index/ in the numbersvar
    i = i + 1  # show that index is increasing with 1

# the range() function

numbersvar = range(5)  # this is a range o to 5
print(numbersvar)  # will print std range (0,5) and if we want all numbers we need to "for loop things

numbers = range(5, 10)
for number in numbers:  # numbers is a known type of variable not any type
    print(number)  # prints each number vertically 5 to 9 (not taking 10)

numbers = range(5, 10, 2)  # 5 is starting number, 9 (not 10) is ending and 2 is the step
for number in numbers:  # numbers is a known type of variable not any type
    print(number)  # prints each number vertically 5 to 9 (not taking 10) but takes 2 per step so 5, 5+2, 7+9,

# this is same as first storing in numbers "numbers = range(0,5. no need for that)
for number in range(5):  # numbers is a known type of variable not any type
    print(number)

# Tuples - cant be changed - immutable. make tupels when you want to have a list in the code that is not changeable/modifiable.

numbers = (1, 2, 3, 3)  # we define tupels with brackets and list of numbers with []
print (numbers.count(3)) #shows how many time 3 is present
print (numbers.index(2)) #shows index of first occurance of an element

 #__XX # are magic methods - see in large course

 # new from coursera
print('hello, python')

import sys #imports system so you can print version from it below
print(sys.version)

print (sys.float_info)

print(type(2))  # should show type

print(float(2))  #convert 2 to be a float (2.0) -

print(type(float(2)))  # should show type
print(type(True))
print(type (2))

print(bool(0))  #cast 0 into a bool False - prints false
print(int(True))  #cast True into a int 1 - prints 1
print(type(6/2))  #prints class  - float
print(type(6//2))  # gives int division

# Let's write an expression that calculates how many hours there are in 160 minutes:
print(160//60)  # 2h

x = 43 + 60 + 16 + 41  # stored x as this expression if you want to see it print x

print(x)

y= x/60
print(y)

x: float= x/2  # overwrite var x with its new value and add type

print(x)

# name variables meaningfully
