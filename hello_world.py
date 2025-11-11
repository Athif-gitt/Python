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

# class Animal:
#     # attribute and method of the parent class
#     name = ""
#
#     def eat(self):
#         print("I can eat")
#
#
# # inherit from Animal
# class Dog(Animal):
#
#     # new method in subclass
#     def display(self):
#         # access name attribute of superclass using self
#         print("My name is ", self.name)
#
#
# # create an object of the subclass
# labrador = Dog()
#
# # access superclass attribute and method
# labrador.name = "Rohu"
# labrador.eat()
#
# # call subclass method
# labrador.display()

# class Animal:
#     def eat(self):
#         print("I can eat!")
#
# class Cat(Animal):
#     def display(self, name):
#         self.name = name
#         print(f"My name is {self.name}")
#
# cat1 = Cat()
# cat1.eat()
# cat1.display("Kitty")

# my_list = [4, 7, 0]
# for element in my_list:
#     print(element)

# create a list of integers
# my_list = [1, 2, 3, 4, 5]
#
# # create an iterator from the list
# iterator = iter(my_list)
# # print(list(iterator))
#
# # iterate through the elements of the iterator
# for element in iterator:
#
#     # Print each element
#     print(element)

# fruits = ["Apple", "Banana", "Cherry"]
# iterator = iter(fruits)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# word = "python"
# i = 0
# while i <= len(word) - 1:
#     print(word[i])
#     i += 1

# def generator(num):
#     n = 0
#     while n < num:
#         yield n
#         n += 1
# for value in generator(5):
#     print(value)

# def generator(value):
#     n = 0
#     while n < value:
#         yield value
#         value += 1
# for value in generator(10):
#     print(value)

# def generator(value):
#     yield value
# print(generator(10))
# for value in generator(10):
#     print(value)

# with open("file1.txt", "r") as file1:
#     content = file1.read()
# print(content)

# with open("file1.txt", "r") as file1:
#     content =file1.read()
# print (content)

# def check_even(numbers):
#     if numbers % 2 == 0:
#         return True
#     return False
# numbers = [1, 2, 3, 4, 5, 6, 7,8 , 9, 10]
#
# even_number_iterator = filter(check_even, numbers)
# print(list(even_number_iterator))

# numbers = [1, 2, 3, 4, 5]
#
#
# def squared(number):
#     return number * number
#
#
# squared_numbers = map(squared, numbers)
# squared_list = list(squared_numbers)
# print(squared_list)

# fruits = ["apple", "banana", "cherry"]
#
# quantities = [5, 10, 7]
#
# result = {fruit.upper(): item * 2 for fruit, item in zip(fruits, quantities)}
#
# print(
#     result)
#
# print(list(zip(fruits, quantities)))

# def simple_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(">>> Starting function execution")
#         result = func(*args, **kwargs)  # Call the original function
#         print(">>> Function execution finished")
#         return result
#     return wrapper
#
# @simple_decorator
# def greet(name):
#     print(f"Hello, {name}!")
#     return f"Greeting for {name}"
#
# @simple_decorator
# def calculate_sum(a, b):
#     print(f"Calculating sum of {a} and {b}")
#     return a + b
#
# # Calling the decorated functions
# print(greet("Alice"))
# print(calculate_sum(10, 20))

# students = {
#     "student1": {"name": "Athif", "marks": 90, "course": "Python"},
#     "student2": {"name": "Arun", "marks": 85, "course": "Java"},
#     "student3": {"name": "Sara", "marks": 95, "course": "C++"}
# }
# for key, value in students.items():
#     print(f"{value['name']} has scored {value['marks']} marks!")
# students["student4"] = {"name": "Ravi", "marks": 80, "Course": "JavaScript"}
# students["student4"]["marks"] = 88
# del(students["student3"])
# print(students)

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return(False)
#         return x
# Solution(121)

# x = 257
# print(id(x))
# y = 257
# print(id(y))

# Problem: Reverse "hello" without slicing.
# word = "hello"
# word_reverse = ""
# for letter in word:
#     word_reverse = letter + word_reverse
# print(word_reverse)

# Problem: Count vowels in "programming".
# word = "programming"
# vowels = "aeiou"
# vowels_sorted = ""
# for letter in word:
#     if letter in vowels:
#         vowels_sorted += letter
# print(len(vowels_sorted))

def square_decorator(func):
    def wrapper(numb):
        print(f"Square of {numb} is:")
        func(numb)
    return wrapper

@square_decorator
def square(numb):
    print(numb ** 2)
square(3)







































