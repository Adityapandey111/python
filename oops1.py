
# que 1
# class Student:

#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
    
#     def display(self):
#         print(f"name : {self.name}\nage : {self.age}\ngrade : {self.grade}")


# student=Student("Aditya",23,7.07)
# student.display()

# <--------------------------- que 2 ---------------------------------->

# class Account:
#     def __init__(self,account_number, account_holder):
#         self.account_number=account_number
#         self.account_holder=account_holder
#         self.balance=0
    
#     def deposite(self,amount):
#         self.balance+=amount

#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#         else:
#             print("Ensufficient balance")
    
#     def display_balance(self):
#         print(f"Balance amount : {self.balance}")
    
# acc1=Account(1234567890,"Aditya")
# acc1.deposite(24000)
# acc1.display_balance()
# acc1.withdraw(15000)
# acc1.display_balance()
# acc1.withdraw(11000)
# acc1.display_balance()

# <-------------------------------que 3------------------------------->

# class Vehicle:
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year
#     def display_info(self):
#         print(f"Name of the brand : {self.brand}\nRelease year : {self.year}")
    
# class Car(Vehicle):
#     def __init__(self, brand, year,name):
#         super().__init__(brand, year)
#         self.name=name
    
#     def display_info(self):
#         print(f"Name of the Brand : {self.brand}\nRelease year of the Car : {self.year}\nName of the Car : {self.name}")

# class Bike(Vehicle):
#     def __init__(self, brand, year,name):
#         super().__init__(brand, year)
#         self.name=name
    
#     def display_info(self):
#         print(f"Name of the Brand : {self.brand}\nRelease year of the Car : {self.year}\nName of the Car : {self.name}")


# car=Car("Tata",2018,"Tigore")
# bike=Bike("Hero",2006,"CD Deluxe")

# car.display_info()
# bike.display_info()

# <------------------------que 4-------------------------->

# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.__price=price
    
#     def setprice(self,price):
#         self.__price=price
    
#     def getprice(self):
#         return self.__price

# product=Product("Skybags",1500)

# print(product.name,product.getprice())

# product.setprice(1001)

# print("Price : ",product.getprice())

# <------------------------- que 5 ------------------------>

# class Shape:
#     def __init__(self):
#         pass
#     def area(self):
#         print("This is the shape class")

# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__()
#         self.radius=radius
    
#     def area(self):
#         return 3.14*self.radius*self.radius

# class Rectangle(Shape):
#     def __init__(self,l,b):
#         super().__init__()
#         self.length=l
#         self.breadth=b
    
#     def area(self):
#         return self.breadth*self.length


# recta=Rectangle(1.5,2)
# circle=Circle(5)

# print(f"Area of the rectangle : {recta.area()}")
# print(f"Area of the circle : {circle.area()}")

# <---------------------------que 6------------------------>

from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary():
        pass

class Full(Employee):
    def __init__(self,basic):
        super().__init__()
        self.basic=basic
    def calculate_salary(self,day):
        return day*self.basic
    
class Part(Employee):
    def __init__(self,basic):
        super().__init__()
        self.basic=basic
    def calculate_salary(self,day):
        return day*self.basic

full=Full(2100)
part=Part(1100)

print(f"Full time salary : {full.calculate_salary(30)}")
print(f"Part time salary : {part.calculate_salary(30)}")