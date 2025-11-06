# words = ["hi", "hello", "world"]
# find_length = list(map(lambda w: len(w), words))
# print(find_length)
#----------------
from logging import raiseExceptions

# import Example
# add_numbers = Example.add(1, 2)
# print(add_numbers)

# try:
#     numerator = 10
#     denomination = 0
#     result = numerator / denomination
#     print(result)
#
#
# except :
#     print("error")

# try:
#     fruits = ["apple", "banana", "litchi"]
#     print(fruits[4])
# except IndexError as e:
#     print("Error", e)

# try:
#     def check_age(age):
#         if age <= 18:
#             raise Exception("under_aged")
#         else:
#             print("aged")
# except:
#     print("error")
# finally:
#     print("execution completed")
#
# check_age(19)

# a = 20
# print(dir())

# a = "python"
# updated = a[1: len(a)]
# print(updated.replace("t", ""))

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
# 
# 
# def ordinary():
#     print("I am ordinary")
# 
# ordinary()

# def outer_func(func):
#     def inner_func():
#         print("outer function")
#         func()
#     return inner_func
#
# def new_func():
#     print("Hi I am func")
#
# a = outer_func(new_func)
# a()

# class Dog:
#     species = "Canine"
#     def __init__(self, name, age, bark):
#         self.name = name
#         self.age = age
#         self.bark = bark
#
# dog1 = Dog("Tobby", 3, "Bow Bow")
# print(dog1.name)
# print(dog1.bark)
# print(dog1.species)
# print(Dog.species)

# class Animals:
#     species = "Animal Kingdon"
#     def __init__(self, kind, age, aggressiveness):
#         self.kind = kind
#         self.age = age
#         self.aggressiveness = aggressiveness
# animal1 = Animals("Monkey", 4, 2)
# animal2 = Animals("donkey", 9, 0)
# print(animal1.age)
# print(Animals.species)
# Animals.species = "changed"
# print(animal1.species)
# print(animal2.species)

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def display(self):
#         print(f"{self.title} is a beutiful book by {self.author} at {self.price} Dollars!")
# book1 = Book ("Rich Dad Poor Dad", "Lewis Hamilton", 499)
# book1.display()

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def display(self):
#         print(f"{self.title} is written by {self.author} priced at {self.price}")
# book1 = Book ("Rich Dad Poor Dad", "Lewis Hamilton", 499)
# book1.display()






















