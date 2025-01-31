# def my_function():
#   print("Hello from a function")


# my_function()



# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")



# x = lambda a : a + 10
# print(x(5))

# def myfunc(n):
#   return lambda a : a * n



# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))


# def myfunc(n):
#   return lambda a : a * n

# mytripler = myfunc(3)

# print(mytripler(11))


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))




# class MyClass:
#   x = 5



#   class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)



# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()


# #By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.



# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019

