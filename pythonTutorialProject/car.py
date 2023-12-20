#Object Oriented Programming in Python.

"""class Car:

    def __init__(self,make,model,year,color):
        #Attributes of the object or what it looks like.
        self.make = make
        self.model = model
        self.year = year
        self.color = color

        #Methods of the object or what it can do.
    def drive(self):
        print("This "+self.model+" is being driven.")

    def stop(self):
        print("The "+self.model+" has stopped moving.")"""

class Car:

    wheels = 4 #class variable declared inside the class outside the constructor [def __init__]

    def __init__(self,make,model,year,color):
        self.make = make #instance variable declared inside the constructor of the class instance.
        self.model = model #instance variable
        self.year = year #instance variable
        self.color = color #instance variable

