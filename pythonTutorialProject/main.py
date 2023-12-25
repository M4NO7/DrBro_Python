"""#HelloWorld
print("Hello Manoj Kothwal")
print("Let's begin a new at learning this shit")

# variable = a container for a value. Behaves as the value that it contains
#String
first_name = "winner"
last_name = "string"
full_name = first_name +" "+ last_name
#print (type (full_name))
print("Hello " + full_name)

#integer and string concat
age = 31
age = age + 1
age  += 1
print("Your age is : " +str(age))
print(type(age))

#floating point numbers

height = 168.90
print("Your height is: "+str(height)+"cms")
print(type(height))

#boolean
human = True
print("Are you a human? : " + str(human))

#multiple assignment = allows us to assign multiple variables at the same time in one line of code

name = "Manoj Kothwal"
age = 31
attractive = True

name, age, attractive = "Manoj Kothwal", 31, True
print(name)
print(age)
print(attractive)

Spongebob = 30
Patrick = 30
Sandy = 30
Squidward = 30

Spongebob = Patrick = Sandy = Squidward = 30

print(Spongebob)
print(Patrick)
print(Sandy)
print(Squidward)

name = "manoj kothwal"

print(len(name))
print(name.find("o"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o","a"))
print(name*10)

#type_casting = convert the data type of a value to another data type

x = 1 #int
y = 2.0 #float
z = "3" #str

y = int(y)
z = int(z)

print(x,int(y%2),int(z*3))

name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

print("Hello "+ name)
print("You are "+str(age)+" years old")
print("And you are "+str(height)+ "cm tall")

import math

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(420))
print(max(pi,x,y,z))
print(min(pi,x,y,z))

#slicing = create a substring by extracting elements from another string
#          indexing[] or slice()
#          [start:stop:step]

#indexing[]
name = "Manoj Kothwal"

first_name = name[0:6]        #  [0:6]
print(first_name)
last_name = name[6:]         #  [6:end]
print(last_name)
funky_name = name[::2]       #  [0:end:2]
print(funky_name)
reversed_name = name[::-1]   #  [0:end:-1]
print(reversed_name)

#slicing()
website1 = "http://google.com"
slice1 = slice(7,-4)
print(website1[slice1])
website2 = "http://wikipedia.com"
slice2 = slice(7,-4)
print(website2[slice2])

#if statement = a block of code that will execute if it's condition is true

age = float(input("How old are you ?: "))

if age >= 100:
    print("You are over a century old!")
elif age >= 18 < 100:
    print("You are an adult!")
elif age >= 0:
    print("You have'nt been born yet!")
elif age <= -1:
    print("You cannot age backwards in time ! Oops !")
else:
    print("You are a child!")

# logical operators (and,or,not) = used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is good today!")
    print("Go outside and enjoy😎")
elif not(temp < 0 or temp > 30):
    print("The temperature is very bad outside")
    print("Better stay inside😒")

# while loop = a statement that will execute it's block of code,
#              as long as it's condition remains true.

while 1==1:
    print("Help ! I am stuck in a loop for eternity")

name = None

while not name:
    name = input("Enter your name: ")

print("Hello "+name)

#for loop = a statement that will execute it's block of code
#           a limited amount of times
#
#           while loop = unlimited
#           for loop = limited

for i in range(10):
    print(i+1)

for i in range(1,100+1,1):
    print(i)

for i in "Manoj Kothwal":
    print(i)

import time

for seconds in range(0,100,1):
    print(seconds)
    time.sleep(1)
print("Yugaadi Habbada Shubhashayagalu")

#nested loops = The "inner loop" will finish all of it's iterations before
#               finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
#        for k in range(rows * columns):
            print(symbol, end = " ")
    print()

# Loop control statements = change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

# for loop above displays only the phone_number digits except the hyphen "-" because of the continue statement
phone_number = "123-456-7890"

for i in phone_number:
    if i == ("-"):
        continue
    print(i, end = "")

# for loop
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end=" ")

# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog","spaghetti","pudding"]

food[4] = "sushi"

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0, "cake")
food.sort()
food.clear() # displays empty list

for x in food:
    print(x,end=" ") # displays x elements in food after  append operation.
print(food,end="") # displays food[] after operations in a list form.

# 2D lists = a list of lists

paaneeya = ["kaafi","soda","chaha","nannari"]
bhojana = ["anna-muddipalya","chapathi-palya","anna-saaru","anna-huli"]
sihithinisugalu = ["mysore pak","shrikhanda","shavige payasa","appi payasa"]

khadya = [paaneeya,bhojana,sihithinisugalu]

print(khadya[0],bhojana[0],sihithinisugalu[0])

# tuple = collection which is ordered and unchangeable
#          used to group together related data

professional = ("Manoj",31,"male")

print(professional.count("Manoj"))
print(professional.index("male"))

for x in professional:
    print(x)

if "Manoj" in professional:
    print("Manoj is here!")
elif "Manoj" not in professional:
    print("Manoj is not here but Manojavam is here!")

# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#dishes.update(utensils)
#dinner_table = utensils.union(dishes)

#print(utensils.difference(dishes))
#print(dishes.intersection(utensils))

#for x in dinner_table:
#    print(x,end=" ")

# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allows us to access a value quickly

capitals = {'USA':'Washington DC','India':'New Delhi',
            'China': 'Beijing','Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals['Germany'])
print(capitals.get('Germany'))

# index operator [] = gives access to a sequence's element (str,list,tuples)
#

name = "manoj kothwal is a brahmana!"

#if(name[0].isupper()):
#    name = name.lower()

first_name = name[0:13].upper()
print(first_name)
last_name = name[0:13].lower()
print(last_name)
last_character = name[-14:]
print(last_character)

#function = a block of code which is executed only when it is called.

def hello(f_name,l_name,age):
    print("Hello "+f_name+" "+l_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day! And quickly get a job before it gets embarassing")

hello("Manoj","Kothwal",31)

# return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as function's return value.

def multiply(number1,number2):
    return number1 * number2

x = multiply(39,789065)

print(x)

# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives

def hello(first,middle,last):
    print("Hello ! "+first+" "+middle+" "+last)

hello(last="Manoj",middle="Kothwal",first="How are you ?")

# nested functions calls = function calls inside other function calls
#                          innermost function calls are resolved first
#                          returned value is used as argument for the next outer function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)


# nested function call takes string input converts it to float takes an absolute value and rounds it off to a nearest value as below.
print(round(abs(float(input("Enter a whole positive number: ")))))

# scope = The region that a variable is recognized
#          A variable is only available from inside the region it is created:
#          A global and locally scoped versions of a variable can be created.

name = "Manoj " # global scope (available inside and outside functions)

def display_name():
   name = "Kothwal" # local scope (available only in this function)
   print(name)

display_name()
print(name)

# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def div(*stuff):
    sum = 1
    stuff = list(stuff)
    stuff[0] = 1
    for i in stuff:
        sum *= i
    return sum
print(div(1,2,3,4,5,6,7,8,9))

# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of [keyword arguments]
# **kwargs means [keyword arguments]

def hello(**kwargs):
    #print("Hello " +kwargs['first'] + "" + kwargs['middle'] + "" + kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
hello(title ="Mr.",first="Manoj ",middle="Kumar ",last="Kothwal ")

# str.format = optional method that gives users
#              more control while displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal,item)) {} - format value
print("The {0} jumped over the {1}".format(animal,item)) #positional arguments
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Manoj Kothwal"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name)) # spaced padding
print("Hello, my name is {:<15}. Nice to meet you".format(name)) # right aligned padding
print("Hello, my name is {:>15}. Nice to meet you".format(name)) # left aligned padding
print("Hello, my name is {:^15}. Nice to meet you".format(name)) # center aligned padding

number = 1000

print("The number pi is {:.3f}".format(number)) # 3 digits after decimal point will be displayed
print("The number is {:,}".format(number)) #, will be displayed after the first digit
print("The number is {:b}".format(number)) # binary equivalent of the number = 1000
print("The number is {:o}".format(number)) # octal equivalent of the number
print("The number is {:X}".format(number)) # hexadecimal equivalent of the number
print("The number is {:E}".format(number)) # scientific notation equivalent of the number


#random module

import random

x = random.randint(1,6) # print random numbers from 1-6
y = random.random() # print random decimal values
print(x)
print(y)

myList = ['rock','paper','scissors']
z = random.choice(myList) # select and print random choice from myList like the game
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards) # deck of cards getting shuffled in random made me play solitaire for half an hour straight.
print(cards)

# exception handling = events detected during execution that interrupt the flow of a program
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide any number by zero :(")
except ValueError as e:
    print(e)
    print("Enter only numbers please !")
except Exception as e:
    print(e)
    print("something is not working :(")
else:
    print(result)
finally:
    print("This will always execute regardless of the exception caught")

import os

path = "C:\\Users\\manoj\\OneDrive\\Desktop\\test\\test1.txt"

if os.path.exists(path):
    print("The location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("The location does not exist!")

# copyfile() = copies contents of file
# copy() = copyfile() + permission mode + destination can be a directory
# copy = copy() + copies metadata (file's creation and modification times)

import shutil

#shutil.copyfile('test2.txt','copy.txt') #src,dst
#shutil.copy('test2.txt','copy1.txt') #src,dst
#shutil.copy2('test2.txt','copy2.txt') #src,dst

import os

source = "test6.txt" #current directory or source directory
destination = "C:\\Users\\manoj\\OneDrive\\Desktop\\test\\test6.txt" #destination directory

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")

import os
import shutil

path = 'folder1'

try:
    #os.remove(path) #delete a file
    #os.rmdir(path) #delete a file or empty folder
    #shutil.rmtree(path) #delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("That folder contains files")
else:
    print(path+" was deleted")

# module = a file containing python code. May contain functions, classes, etc.,
# Used with modular programming, which is to prepare a program into parts

#3:10:13 timestamp on BroCode Python Video Tutorial
#import messages
#import messages as m
#from messages import hello,bye
#from messages import * (this one is dangerous)

#help("modules")

#import messages as msg
from messages import *

hello()
bye()

#help("statistics")
#help("pickle")


import random

while True:
    choices = ["rock","paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock,paper, or scissors?: ").lower()

    if player == computer:
        print("computer: " ,computer)
        print("player:" ,player)
        print("Tie!")
    #player choice rock
    elif player == "rock":
        if computer == "paper":
            print("computer: ",computer)
            print("player:", player)
            print("You lose:")
        if computer == "scissors":
            print("computer: ", computer)
            print("player:", player)
            print("You win: ")
    #player choice scissors
    elif player == "scissors":
        if computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("You lose:" )
        if computer == "paper":
            print("computer:", computer)
            print("player:", player)
            print("You win!:",)
    #player choice paper
    elif player == "paper":
        if computer == "scissors":
            print("computer:", computer)
            print("player:", player)
            print("You lose:")
        if computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("You win:")


    play_again = input("Play again? (yes/no): ").lower()

    if play_again == "no":
        break

print("Bye!")

#Quiz_Game

#def new_game():
#   pass
#def check_answer():
#    pass
# def display_score():
#    pass
# def play_again():
#   pass

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#-------------------------------------------------------------------

def check_answer(answer, guess):

    if answer == guess:
        print("RIGHT")
        return 1
    else:
        print("WRONG")
        return 0

#-------------------------------------------------------------------

def display_score(correct_guesses, guesses):
    print("-------------------------------")
    print("Results")
    print("-------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is:  "+str(score)+"%")


# -------------------------------------------------------------------

def play_again():
    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is Earth round?: ": "A"
}

options = [["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A . 1989", "B . 1991", "C. 2000", "D . 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False","C. Sometimes","D. What's Earth?"]]


new_game()

while play_again():
    new_game()

print("Goodbye!")

#03:35:36

#Object Oriented Programming in Python

from car import Car
#from the name of the module {car} import the class {Car}

car_1 = Car("Chevy","Corvette",2023,"blue")
car_2 = Car("Ford","Mustang",2022,"red")
car_3 = Car("Hindustan Motors","Contessa",1976,"dark blue")

Car.wheels = 2
#car_1.wheels = 3 #instance variable altered to suit output
#car_3.wheels = 1 #same as above

print(car_1.wheels,"car_1  is an auto")
print(car_2.wheels)
print(car_3.wheels,"car_3 is an monocycle")

print(Car.wheels) #Displaying unchanged class variable from {car} module and {Car} class from car.py

#print("This is the First Car Method:")
#print(car_1.make)
#print(car_1.model)
#print(car_1.year)
#print(car_1.color)
#car_1.drive()
#car_1.stop()

#print("This the Second Car Method:")
#print(car_2.make)
#print(car_2.model)
#print(car_2.year)
#print(car_2.color)
#car_2.drive()
#car_2.stop()

#Inheritance in Object Oriented Programming
class Animal:

    alive = print("The animal is alive:",True)

    def eat(self):
        print("The animal is eating")

    def slumber(self):
        print("The animal is sleeping")

    def reproduce(self):
        print("The animal is reproducing")

class Rabbit(Animal):

    def run(self):
        print("The rabbit is running")

class Fish(Animal):

    def swim(self):
        print("The fish is swimming")

class Hawk(Animal):

    def fly(self):
        print("The hawk is flying")


print(Rabbit.alive)
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
rabbit.eat()
rabbit.slumber()
rabbit.reproduce()

fish.swim()
fish.eat()
fish.slumber()
fish.reproduce()

hawk.fly()
hawk.eat()
hawk.slumber()
hawk.reproduce()

#multi-level inheritance = when a derived (child) class inherits another derived (child)

class Organism:

    alive = True

    def reproduce(self):
        print("This animal is reproducing")

class Animal(Organism):
#Animal extends from Organism

    def eat(self):
        print("The animal is eating")

class Dog(Animal):
#Dog exentds from Animal and in turn extends from Organism

    def bark(self):
        print("This dog is barking")

class Amoeba(Organism):

    def split_cell(self):
        print("Amoeba is a single-cell organism and it reproduces by splitting itself")

dog = Dog()
amoeba = Amoeba()
print(dog.alive)
dog.reproduce()
dog.eat()
dog.bark()
amoeba.reproduce()
amoeba.split_cell()

#multiple inheritance = when a child class is derived from more than one parent class.

class Prey:

    def flee(self):
        print("An animal which is a prey flees when in danger.")


class Predator:

    def hunt(self):
        print("An animal which is a predator hunts when hungry.")

class PreyPred:

    def hunternhunted(self):
        print("An animal which is both a prey and a predator depending on circumstances.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(PreyPred):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunternhunted()

#Method Overriding in programming = overriding the method of a parent class in a
# derived(child) class as many times as there is.

class Animal:

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("All animals need to sleep to rest and recuperate")

class Rabbit(Animal):
    def eat(self):
        print("Rabbits eat carrot for food")


class Stout(Animal):
    def eat(self):
        print("Stouts hunt rabbit for food")

class Molerat(Animal):
    def dig(self):
        print("Molerat dig underground homes for shelter and protection of young ones")

rabbit = Rabbit()
stout = Stout()
molerat = Molerat()

rabbit.eat()
rabbit.sleep()
#common method sleep() for all animal classes.

molerat.eat()
molerat.dig()
molerat.sleep()

stout.eat()
stout.sleep()

#method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self.

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the car")
        return self

car = Car()
car.turn_on()\
   .drive()\
   .brake()\
   .turn_off()

# method chained in sequence for execution one after the other.
#\ line continuation character.

#super = Function used to give access to the methods of a parent class.
#        Returns a temporary object of a parent class when used.

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length, width):
        #calling parent class init method termed super() class
        super().__init__(length, width)

    def area(self):
        return self.length*self.width


class Cube(Rectangle):

    def __init__(self, length, width, height):
        #calling parent class init method termed super() class
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())

#Prevents a user from creating an object of that class.
#+compels a user to override abstract methods in a child class.

#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implementation.


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()

#Passing Objects as arguments. car() and motorcycle (bike) objects as argument to match with vehicle.
# color method.

class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle, color):

    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1, "red")
change_color(car_2, "black")
change_color(car_3, "maroon")

change_color(bike_1, "magenta")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)

#Duck typing = concept where the class of an object is less important than the methods/attributes.
#              class type is not checked if minimum methods/attributes are present.
#              "If it walks like a duck, and it quacks like a duck, then it must be a duck"
# Method is important than the class it comes from.

class Bird:


    def talk(self):
        pass

    def walk(self):
        pass


class Duck(Bird):

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken(Bird):

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person:

    def catch(self, duck, chicken):
        duck.talk()
        chicken.talk()
        print("You caught the critter!")

bird = Bird()
chicken = Chicken()
duck = Duck()
person = Person()

person.catch(chicken, duck)

#04:27:39 timestamp
#walrus operator :=

#new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# foods = list()
# while True:
#    food = input("What food do you like?: ")
#        if food == "quit":
#            break
#   foods.append(food)

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

#def hello():
#    print("Hello")

#print(hello)
#hi = hello
#hello()
#hi()

#print(hi)
say = print
say("Whoa! I can't believe this works! :O") # say is equivalent to print() statement."""

# Higher Order Function = a function that either:
#                          1. accepts a function as an argument
#                         or
#                          2. returns a function
#                           (In python, functions are also treated as objects)
"""def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(quiet)
hello(loud)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))

# lambda functions = function written in 1 line using lambda keyword
#                    accepts any number of arguments, but only has one expression.
#                    (think of it as a shortcut)
#                    (useful if needed for a short period of time, throw-away)
#   lambda parameters:expression

#double = lambda x: x * 2
#print(double(100))
#multiply = lambda x, y: x * y
#print(multiply(1000, 1000))
#add = lambda x, y, z: x + y + z
#print(add(-512, -512, -512))
#full_name = lambda first_name, last_name: first_name+" "+last_name
#print(full_name("Manoj Kumar", "Kothwal"))
#age_check = lambda age: True if age >= 18 else False
#print(age_check(18))

#sort() method  = used with lists
#sort() function = used with iterables

#students = ("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")
#students.sort(reverse=True)
#sorted_students = sorted(students, reverse=True)

#for i in sorted_students:
#   print (i)
#Column numbers 0          1   2
#students = [("Squidward", "F", 60),
#            ("Sandy","A", 33),
#            ("Patrick", "D", 36),
#            ("Spongebob","B", 20),
#            ("Mr.Krabs","C", 78)]

#grade = lambda grades:grades[2]
#students.sort(key=grade,reverse=True)
#students.sort()

#() - list
#[] - tuple
students = (("Squidward", "F", 60),
            ("Sandy","A", 33),
            ("Patrick", "D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

age = lambda ages:ages[2]
sorted_students = sorted(students,key=age)

for i in sorted_students:
    print(i)

# map() = applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

#columns     0      1
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
          ("socks",10.00)]

#to_euros = lambda data: (data[0],data[1]*0.82)
to_dollars = lambda data: (data[0], data[1]/0.82)


#store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))

#for i in store_euros:
for i in store_dollars:
    print(i)

# filter() = creates a collection of elements from an iterable for which a function returns true
#
#filter(function, iterable)
#columns        0     1
friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

#age = lambda data:data[1] >= 18
age = lambda data:data[1] < 18
#drinking_buddies = list(filter(age, friends))
teetotaler_buddies = list(filter(age,friends))

for i in teetotaler_buddies:
    print(i)

#reduce = apply a function to an iterable and reduce it to a single cumulative value.
#          performs function on first two elements and repeats process until 1 value remains
#
#reduce(functions, iterable)

import functools

#letters = ["H","E","L","L","0"]
#word = functools.reduce(lambda x, y,:x + y,letters)
#print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y,:x * y,factorial)
print(result)

#list comprehension = a way to create a new list with less syntax
#                     can mimic certain lambda functions, easier to read
#                     list = [expression for item in iterable]
#                     list = [expression for item in iterable if conditional]
#                     list = [expression if/else for item in iterable]

squares = []                  #  create an empty list
for i in range(1,1000):       #  create a for loop
    squares.append(i*i)       #  define what each loop iteration should do
print(squares)

same result as above using list comprehension
#squares = [i * i for i in range(1,100000000)]
#print(squares)

#students = [100,90,80,70,60,50,40,30,0]

#passed_students = list(filter(lambda x: x >= 50, students))
#passed_students = [i for i in students if i >= 60]
#passed_students = [i if i >= 60 else "FAILED" for i in students]
#print(passed_students)

# ------------------------------------------------------------------------------
# dictionary comprehension = create dictionaries using an expresssion
#                           can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# Fahrenheit
# Celsius
# ------------------------------------------------------------------------------------
# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)
# ------------------------------------------------------------------------------------
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value != "sunny" and value != "snowing"}
# sunny_weather = {key: value for (key,value) in weather.items() if value != "cloudy" and value != "snowing"}
# print(sunny_weather)
# ------------------------------------------------------------------------------------------
# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)
# ------------------------------------------------------------------------------------------
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)

# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element within the zip obejct.
#

# timestamp:- 05:20:00
usernames = ["Dude", "Bro", "Mister","Manoj"]
passwords = ("p@ssword", "abc123", "guest","Kothwal")
login_date = ["1/1/2021","2/2/2022","3/3/2023","4/4/2024"]
# dict and zip keywords to create a dictionary of the zipped key values from both usernames and passwords.
#users = dict(zip(usernames, passwords, login_date))
#print(type(users))
#for key,value in users.items():
#print(key+" : "+value)

users = zip(usernames, passwords, login_date)
for i in users:
    print(i)

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's
# the intitial module being run.

def main():
    print("Calling main function!")

def secondary():
   print("Calling second main function!")

if __name__ == '__main__':
    main()
#if __name__ != '__main__':
    secondary()
#    else
#        secondary()

# --------------------------
#  if __name__ == '__main__'
# --------------------------

# y tho ?
# 1. Module can be run as standalone program
# 2. Module can be imported and used by other modules

# Python interprets sets "special variables", one of which __name__
# then Python will execute the code found within __main__

import max_num
import car

# printing the name of the __main__ from max_num module
print(max_num.__name__)
print(car.__name__)
if __name__ == '__main__':
    pass
print(__name__)

if __name__ == '__main__':
    print("running this module directly")
else:
    print("running other module indirectly")

# ************************
import time
# ************************

#print(time.ctime(0)) # convert a time expressed in seconds since a epoch to a readable string
                      # epoch = when your computer thinks time began(reference point)
#print(time.time())   # returns current seconds since epoch
#print(time.ctime(time.time()))  # will get current time


# *****************************************************
#time_object = time.localtime() # local time
#time_object = time.gmtime() # UTC time
# time.strftime(format, time_object) formats a time_object to a string
#local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
#print(local_time)
# *****************************************************

#time_string = "23 March, 2023"
#time_object = time.strptime(time_string,"%d %B %Y")
#print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2023,10,27,6,49,0,0,0,0)
time_string1 = time.asctime(time_tuple)
time_string2 = time.mktime(time_tuple)
print(time_string1, time_string2)

# thread = a flow of execution. Like a separate order of instructions.
#               However each thread takes a turn running to achieve concurrency
#               GIL = (global interpreter lock),
#               allows only one thread to hold the control of the Python interpreter at any one time
# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing
# io bound = program/task spends most of it's time waiting for external events (user inputs, web scraping)
#            use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(5)
    print("You drank coffee")

def study():
    time.sleep(7)
    print("You finished your homework")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

#eat_breakfast()
#drink_coffee()
#study()

print(threading.active_count())
print("Main thread here:- ",threading.enumerate())
print(time.perf_counter(),"seconds")

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(0.1)
        count += 0.1
        print("logged in for",count,"seconds")
#
# x = threading.Thread(target=timer)
x = threading.Thread(target=timer, daemon=True)
x.start()
# x.setDaemon(False)
# print(x.isDaemon())
#
answer = input("Do you wish to exit ?")

# --------------------------------
# Python Multiprocessing
# -------------------------------
# multiprocessing = running tasks in parallel on different cpu cores, bypass GUI used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
#    pass

    print(cpu_count())

    a = Process(target=counter, args=(125000000,))
    b = Process(target=counter, args=(125000000,))
    c = Process(target=counter, args=(125000000,))
    d = Process(target=counter, args=(125000000,))
    e = Process(target=counter, args=(125000000,))
    f = Process(target=counter, args=(125000000,))
    g = Process(target=counter, args=(125000000,))
    h = Process(target=counter, args=(125000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    print("finished in:",time.perf_counter(),"seconds")

if __name__ == '__main__':
    main()
#   print(__name__)

from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets


window = Tk() #instanitate an instance of a window
window.geometry("420x420")
window.title("My first GUI Program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop() # place window on computer screen, listen for events

from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

icon = PhotoImage(file='person.png')
window.iconphoto(True,icon)

label = Label(window,
              text="bro, do you even code?",
              font=('Arial',30,'bold'),
              fg='black',
              bg='black',
              relief=RAISED,
              bd=20,
              padx=20,
              pady=20,
              image=icon,
              compound='center')

label.pack()

window.mainloop()

from tkinter import *
# button = you click it, then it does stuff
count = 0
def click():
    global count
    count += 5
    print("The button has been clicked this many times:",count)
window = Tk()
photo = PhotoImage(file='person.png')
button = Button(window,
                text="click me!",
                command=click,
                font = ("Comic Sans",30),
                fg="Sky Blue",
                bg="Black",
                activeforeground="Sky Blue",
                activebackground="Dark Blue",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()
window.mainloop()

from tkinter import *

# entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print("Hello " +username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Arial",20),
              fg="Dark Green",
              bg="Black",
              show="#")

#entry.insert(0,'SR-71 Blackbird')

entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=LEFT)

backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=LEFT)

window.mainloop()

from tkinter import *

def display():
    if(x.get() == 1):
#    if(x.get()): for on and off values which are boolean in type
#    if(x.get()=="Yes"): for on and off values which are string in type
        print('You agree!')
    else:
        print("You don't agree:(")

window = Tk()

x = IntVar()

#python_photo = PhotoImage(file='person.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
#                          onvalue="True",
#                          offvalue="False",
#                          onvalue="Yes",
#                          offvalue="No"
                           onvalue=1,
                           offvalue=0,
                           command=display,
#                          image=python_photo,
                           font=('Cambrian',20),
                           fg="Dark Red",
                           bg="Sky Blue",
                           state=ACTIVE,
                           activeforeground="White",
                           activebackground="Sky Blue",
                           padx=25,
                           pady=10)

check_button.pack()
window.mainloop()

from tkinter import *

# radio button = similar to checkbox, but you can only select one from a group.

oota = ["anna","saaru","chutney","muddipalya","mosaru"]

def order():
    if(x.get() == 0):
        print("You ordered a plate of Anna")
    elif(x.get() == 1):
        print("You ordered a bowl of Saaru")
    elif(x.get() == 2):
        print("You ordered a bowl of chutney")
    elif (x.get() == 3):
        print("You ordered a bowl of muddipalya")
    elif (x.get() == 4):
        print("You ordered a bowl of mosaru")
    else:
        print("Yenu beku ootakka mattha ??????")

window = Tk()

#annaImage = PhotoImage(file='anna.png')
#saaruImage = Photoimage(file='saaru.png')
#chutneyImage = PhotoImage(file='chutney.png')
#muddipalyaImage = PhotoImage(file='muddipalya.png')
#mosaruImage = PhotoImage(file='mosaru.png')
#ootaImages = [annaImage,saaruImage,chutneyImage,muddipalyaImage,mosaruImage]

x = IntVar()

for index in range(len(oota)):
    radiobutton = Radiobutton(window,
                              text=oota[index], # adds text to radiobuttons
                              variable=x, # groups radiobuttons together if they share the same variable
                              value=index, # assigns each radiobutton a different value
                              padx = 25, # adds padding on x-axis
                              #pady = 25, # adds padding on y-axis
                              font = ("Arial",15),
                              indicatoron=0, # eliminate circle indicators
                              width = 10, # sets width of radiobuttons
                              command = order # set command of radiobutton to function. (mapping food item to its function)
                              )

    radiobutton.config()
    radiobutton.pack(anchor=W)

window.mainloop()

# --------------------------------------------------------------------------------------------------------------------
#                             'oota' generally means food in Kannada Language [pronounced - oo-taa]
#                             image = ootaImages[index] # adds image to radiobutton with their corresponding names
#                             compound = 'left' # adds image and text to the (left-side)

#                             Did not use the images of Oota as mentioned above because was busy learning python offline
#                             did not want loose focus by going online on the pc.
#                             People are free to add their own food culture images for studying and learning the actions
#                             of radiobutton in Python using tkinter.
# ----------------------------------------------------------------------------------------------------------------------

# Scale in Python using Tkinter GUI

from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")

window = Tk()

#hotImage = PhotoImage(file='logo.png')    # To set the icon on the top of the scale as a flame showing hot weather
#hotLabel = Label(image=hotImage)
#hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL, # orientation of the scale to be visualized
              font = ('Consolas',18), # font types and size on the scale
              tickinterval = 10, # value at each interval of the scale on the GUI.
#             showvalue = 0, # hide current value
              resolution = 5, # increment of slider
              troughcolor = "sky blue",
              fg = "white",
              bg = "black",
              )

# scale.set(50)
scale.set(((scale['from']-scale['to'])/2)+scale['to']) # keeps scale indicator always in the middle w.r.t to the value at the top
scale.pack()

# coldImage = PhotoImage(file='cold.png') # To set the icon on the bottom of the scale as a snowflake showing cold weather
# coldLabel = Label(image=coldImage)
# coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()
window.mainloop()


# -------------------------------------------------------------------------------------------------
# lightbox = A listing of selectable text items within it's own container

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    if (listbox.index == 0):
        print("Kindly select an item from the list : ")
    else:
        print("You have ordered a : ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
   listbox.delete(listbox.curselection()) # To delete individual selected items from the list
    listbox.config(height=listbox.size())

#def delete():
#   for index in reversed(listbox.curselection()): # To delete multiple selections from the food[] item list.
#        listbox.delete(index)


from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",25),
                  width=15,
                  height=12,
                  selectmode=MULTIPLE,
                  )
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"hamburger")
listbox.insert(3,"hotdog")
listbox.insert(4,"chowder")
listbox.insert(5,"pancakes & syrup")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="submit",command=submit)
submitButton.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack()

window.mainloop()

# --------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import messagebox  # import messagebox library

def click():

    #messagebox.showinfo(title = 'Not ok',message = 'You are a person whose unemployed') # info messagebox
    #messagebox.showwarning(title='WARNING !!!',message='Your network is under attack') # warning messagebox
    #messagebox.showerror(title='ERROR !!!',message = 'Something went wrong') # error messagebox

    #if messagebox.askokcancel(title='ask ok cancel',message = 'Do you want to do the thing ?'): # ask ok cancel messagebox
        #print('You did the thing (:_:)') # after clicking ok
    #else:
        #print('You chose not to do the thing (;_;)') # after clicking cancel

    #if messagebox.askretrycancel(title = 'ask retry cancel',message = 'Do you want to retry the thing ?'):
        #print('You just clicked retry')
    #else:
       #print('You clicked to cancel')

    #if messagebox.askyesno(title='ask yes or no',message='Do you like Jalebi ?'):
        #print('You like Jalebi :)')
    #else:
        #print('You definitely do not like Jalebi :(')

        #print(messagebox.askquestion(title='ask a question',message='Do you like Paayasa ?'))
    #answer =  messagebox.askquestion(title='Ask a question ?',message='Do you like Paayasa ?')
    #if(answer == 'yes'):
        #print('So your a man of tradition !!!')
    #else:
        #print('So you do not like Traditional Indian Desserts ?'
              #'clearly your missing out on some wonderful stuff')

    answer = messagebox.askyesnocancel(title='Yes No Cancel',message='Do you like to code ?')
    if(answer == True):
        print("You like to code :)")
    elif(answer == FALSE):
        print("You do not like to code stop watching this video !!! Yo....:(  :(")
    else:
        print("You seem uninterested so sorry to bother you")

window = Tk()

button = Button(window,command=click,text='click here')
button.pack()

window.mainloop()

# -------------------------------------------------------------------------------------------------


from tkinter import *
from tkinter import colorchooser #submodule

def click():
    color = colorchooser.askcolor() # assign color to a variable
    print(color)
    colorHex = color[1] # assigns element at index 1 to a variable
    print(colorHex)
    window.config(bg=colorHex) # change background color

    #window.config(bg=colorchooser.askcolor()[1]) # change background color

window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()
window.mainloop()

# text widget = functions like a text area, where you can enter multiple lines of text
from tkinter import *


def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()
text = Text(window,
            bg = "Green",
            font = ("Arial",15),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg='purple')
text.pack()
button = Button(window,text='submit',command=submit)
button.pack()
window.mainloop()


# File Functions in Python
from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\manoj\\OneDrive\\Desktop\\Cover Letter",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                                      ("all files","*.*")))

    file = open(filepath,'r')
    print(file.read())
    file.close()

window=Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()

# ------------------------------------------------------------------------------------------------------

# File manipulation functions in Python

from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\manoj\\OneDrive\\Desktop\\Cover Letter",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file",".html"),
                                        ("All files",".*"),
                                    ])

    if file is None:
        return
    filetext = str(text.get(1.0,END))
    #filetext = input("Enter some text I guess : ")
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text='save',command= saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()

# ------------------------------------------------------------------------------------------------------

# Menu Bar in Python

from tkinter import *

def openFile():
    print("File has been opened!")

def saveFile():
    print("File has been closed")
# ------------------------------------------------------------------------------------------------------

def cut():
    print("File has been removed and ready to be placed")

def copy():
    print("File has been copied and ready to be pasted")

def paste():
    print("File has been pasted here")

window = Tk()

#openImage = PhotoImage(file="file.png")
#saveImage = PhotoImage(file="save.png")  [ To add images for functions open, save & quit from file manipulation ]
#exitImage = PhotoImage(file="exit.png")


menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label="File",menu=fileMenu,font=("MV Boli",10))
#fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left') [To add images to the respective functions]
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)
#if(Label == exit):
#    print("File operation completed")

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label="Edit",menu=editMenu,font=("MV Boli",10))
editMenu.add_command(label="Cut",command=cut)
editMenu.add_separator()
editMenu.add_command(label="Copy",command=copy)
editMenu.add_separator()
editMenu.add_command(label="Paste",command=paste)

window.mainloop()

# ------------------------------------------------------------------------------------------------------

# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="green",bd=9,relief=SUNKEN)
frame.place(x=0,y=0)
#frame.pack(side=TOP)

Button(frame,text="W",font=("Arial",15),width=3).pack(side=TOP)
Button(frame,text="A",font=("Calibri",15),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Italic",15),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Cyrillic",15),width=3).pack(side=LEFT)

#button.pack()
window.mainloop()


# ------------------------------------------------------------------------------------------------------

# Creating window using Tkinter

from tkinter import *

def create_window():
    new_window = Tk()   # Or new_window = Toplevel()[new window 'on top' of other windows, linked to a 'bottom' window]
                        # Tk() = new independent window

    print("A new window has been created")

#def close_window():
#    new_window.mainloop()
#    print("All three windows closed")

    #old_window.destroy()   # close out of old_window or main window/bottom window
    #print("The old window is deleted from the memory concurrently")

old_window = Tk()
Button(old_window,text="create new window",command=create_window).pack()

old_window.mainloop()

# ------------------------------------------------------------------------------------------------------

# A notebook widget using tkinter in Python to control other windows

from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)   # widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab1
tab2 = Frame(notebook) #new frame for tab2
tab3 = Frame(notebook) #new frame for tab3 [exit frame]

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.add(tab3,text="Tab 3")
notebook.pack(expand=True,fill="both")  # expand = expand to fill any space not otherwise
                                        # fill = fill space on x and y axis

Label(tab1,text="Hello, This is Tab#1",width=50,height=25).pack()
Label(tab2,text="Hello there, This is Tab#2",width=50,height=25).pack()
Label(tab3,text="Exit Frame Window",width=50,height=25).pack()

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

# grid() = geometry manager that organizes widgets in a table-like structure in a
window = Tk()

titleLabel = Label(window,text="Enter your info",font=("Arial",15)).grid(row=0,column=0)

firstNameLabel = Label(window,text="First name: ",width=20,bg="white").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ",bg="white").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text="email:",bg="white").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=1,columnspan=2)

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# Download button animation using tkinter.

from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.10)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=VERTICAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
textLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# canvas drawing in python using tkinter.
# canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
canvas.create_line(0,0,500,500,fill="blue",width=5)
canvas.create_line(0,500,500,0,fill="red",width=5)
canvas.create_rectangle(50,50,250,250,fill="purple")
points = [250,0,500,500,0,500]
canvas.create_polygon(250,0,500,500,0,500,fill="yellow",outline="black",width=5)
canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(180,180,300,300,fill="white",width=10)

canvas.pack()
window.mainloop()

#----------------------------------------------------------------------------------------------------------------------
# A key event = It performs a function when a key or button is pressed.
#
from tkinter import *

def doSomething(event):
    print("You pressed:"+ event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>",doSomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# Mouse Events = Functions corresponding to any mouse action.

from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " +str(event.x)+","+str(event.y))

window = Tk()

#window.bind("<Button-1>", doSomething) #leftmouseclick
#window.bind("<Button-2>", doSomething) #scrollwheel
#window.bind("<Button-3>", doSomething) #rightmouseclick
#window.bind("<ButtonRelease>", doSomething)
#window.bind("<Enter>", doSomething) #enterthewindow
#window.bind("<Leave>", doSomething) #leavethewindow
#window.bind("<Motion>", doSomething) #Wherethemousemoved

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# drag and drop widgets in python.

from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()

widget = Label(window, bg="red", width=10, height=5)
widget.place(x=0, y=0)

widget.bind("<Button-1>", drag_start)
widget.bind("<B1-Motion>", drag_motion)

widget = Label(window, bg="blue", width=10, height=5)
widget.place(x=77, y=77)

widget.bind("<Button-1>", drag_start)
widget.bind("<B1-Motion>", drag_motion)

widget = Label(window, bg="red", width=10, height=10)
widget.place(x=154, y=154)

widget.bind("<Button-1>", drag_start)
widget.bind("<B1-Motion>", drag_motion)

widget = Label(window, bg="blue", width=10, height=10)
widget.place(x=308,y=308)

widget.bind("<Button-1>", drag_start)
widget.bind("<B1-Motion>", drag_motion)

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# moving png images across the canvas
from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-50)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+50)

def move_left(event):
    label.place(x=label.winfo_x()-50, y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+50, y=label.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Right>",move_right)
window.bind("<Left>",move_left)

myimage = PhotoImage(file='car-icon.png')
label = Label(window,image=myimage)
label.place(x=0,y=0)

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# drawing on canvas using tkinter.

from tkinter import *

def move_up(event):
    canvas.move(myimage,0,-10,)
def move_down(event):
    canvas.move(myimage,0,10)
def move_right(event):
    canvas.move(myimage,10,0)
def move_left(event):
    canvas.move(myimage,-10,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

canvas = Canvas(window,width=800,height=800)
canvas.pack()

photoimage = PhotoImage(file='car-icon.png')
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# animating icons/images on an interactive canvas.

from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 6
yVelocity = 4
window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_image = PhotoImage(file='Space.png')
background = canvas.create_image(0,0,image = background_image,anchor=NW)

photo_image = PhotoImage(file='100x100_black_and_white_pixels.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH - image_width) or coordinates[0]<0):
        xVelocity = -xVelocity

    if(coordinates[1]>=(HEIGHT - image_height) or coordinates[1]<0):
        yVelocity = -yVelocity

    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# Multiple object animations in Python

from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,'white')
basket_ball = Ball(canvas,0,0,100,4,3,'orange')
tennis_ball = Ball(canvas,0,0,25,6,5,'green')
leather_ball = Ball(canvas,0,0,25,9,10,'brown')
pingpong_ball = Ball(canvas,0,0,10,3,15,'black')

while True:
    volley_ball.move()
    basket_ball.move()
    tennis_ball.move()
    leather_ball.move()
    pingpong_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()


# ----------------------------------------------------------------------------------------------------------------------
# Animate a clock with tkinter.

from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

window = Tk()

time_label = Label(window,font=("Calibri",50),fg="#00FF00",bg="black")
time_label.pack()

day_label = Label(window,font=("Calibri",50),fg="#00FF00",bg="black")
day_label.pack()

date_label = Label(window,font=("Calibri",50),fg="#00FF00",bg="black")
date_label.pack()

update()

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# Python email test.

import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"
subject = "Python email test"
body = "I wrote an email! :D"

#header
#triple-quotes begin on next line
#message = f"""#From: Snoop Dogg{sender}
#To :  Nicholas Cage{receiver}
#Subject: {subject}\n
#{body}
""" #triple-quotes end

server = smtplib.SMTP("smtp.gmail.com", 587) #default mail submission port:587
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")


# ----------------------------------------------------------------------------------------------------------------------
# Python Calculator

from tkinter import *

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():
    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:
        equation_label.set("Syntax Error")

        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("arithmetic error")

        equation_text = ""

def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()
window.title("Calculator Program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,height=4,width=9,font=35,
                 command= lambda: button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text=2,height=4,width=9,font=35,
                 command= lambda: button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text=3,height=4,width=9,font=35,
                 command= lambda: button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,height=4,width=9,font=35,
                 command= lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame,text=5,height=4,width=9,font=35,
                 command= lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame,text=6,height=4,width=9,font=35,
                 command= lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,height=4,width=9,font=35,
                 command= lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame,text=8,height=4,width=9,font=35,
                 command= lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame,text=9,height=4,width=9,font=35,
                 command= lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame,text=0,height=4,width=9,font=35,
                 command= lambda: button_press(0))
button0.grid(row=3,column=0)

plus = Button(frame,text='+',height=4,width=9,font=35,
              command= lambda: button_press('+'))
plus.grid(row=0,column=3)

minus = Button(frame,text='-',height=4,width=9,font=35,
               command= lambda: button_press('-'))
minus.grid(row=1,column=3)

multiply = Button(frame,text='*',height=4,width=9,font=35,
                  command= lambda: button_press('*'))
multiply.grid(row=2,column=3)

divide = Button(frame,text='/',height=4,width=9,font=35,
                command= lambda: button_press('/'))
divide.grid(row=3,column=3)

equal = Button(frame,text='=',height=4,width=9,font=35,
                command=equals)
equal.grid(row=3,column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command= lambda: button_press('.') )
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35,
                 command=clear)
clear.pack()

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# Text editor in Python

import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title='pick a color or else')
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    window.title("Untitled Text Editor")
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])

    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")

        text_area.insert(1.0, file.read())

    except  Exception:
        print("Could'nt read file")

    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("Could'nt save file")

        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("About this program", "This is a program written by Manoj Kothwal")
    print("The details about the Text editor written in Python using Tkinter library")
    quit() #calling one function from inside another function

def quit():
    window.destroy()

window = Tk()

window.title("Text Editor Program")
file = None
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height,x,y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)


frame = Frame(window)
frame.grid()

color_button = Button(frame, text='color', command=change_color)
color_button.grid(row=0,column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1,to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0,column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About - The Python Text editor", command=about)

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# Tic-Tac_Toe in Python.

from tkinter import *
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(player[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text=(" Tie!"))

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return 'Tie'

    else:
       return False

def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text= player + "turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas',40) , width=5, height=2,
                                      command= lambda row=row,column=column: next_turn(row,column))
        buttons[row][column].grid(row=row, column=column)
window.mainloop()

# never name your classes with keywords

# ----------------------------------------------------------------------------------------------------------------------
# Snake game in Python

from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 600
SPEED = 100
SPACE_SIZE = 25
BODY_PARTS = 4
SNAKE_COLOR = "#00FF00" #GREEN
FOOD_COLOR = "#FF0000" #RED
BACKGROUND_COLOR = "#000000" #BLACK

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0,(GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collision(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right': #for 180 degree turn backwards
                direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collision(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print("GAME OVER")
        return True

    elif y < 0 or y >= GAME_HEIGHT:
         print("GAME OVER")
         return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True

    return False

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

window = Tk()
window.title("Snake Game in Python using tkinter library")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('Tahoma', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>',lambda event: change_direction('left'))
window.bind('<Right>',lambda event: change_direction('right'))
window.bind('<Up>',lambda event: change_direction('up'))
window.bind('<Down>',lambda event: change_direction('down'))

snake = Snake() #Calling snake constructor
food = Food() #Calling food constructor

next_turn(snake,food)

window.mainloop()

#----------------------------------------------------------------

print("Hello World")"""

