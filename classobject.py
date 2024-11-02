# Define a class
class Car:
    # Constructor method to initialize attributes
    def __init__(self, make, model):
        self.make = make  # Attribute
        self.model = model  # Attribute

    # Method to display car details
    def display_info(self):
        print(f"Car: {self.make} {self.model}")

# Create an object (instance) of Car
car1 = Car("Toyota", "Camry")

# Access object's attributes and methods
print(car1.make)  # Output: Toyota
car1.display_info()  # Output: Car: Toyota Camry

# Parent class
class Animal:
    def sound(self):
        return "Some sound"

# Child classes inheriting from Animal
class Dog(Animal):
    def sound(self):  # Overriding method
        return "Woof!"

class Cat(Animal):
    def soundthanks(self):  # Overriding method
        return "Meow!"

# Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())  # Output: Woof!, Meow!


""" simple encapsulation class using private variable __ """

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid amount or insufficient balance")

    def get_balance(self):
        return self.__balance

# Testing encapsulation
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300
""" print(account.__balance)  # Error:  Because is pricate  AttributeError, private attribute """
