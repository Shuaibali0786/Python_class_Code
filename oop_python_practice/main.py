# class Student:
    
#     def __init__(self, fullname):
#         self.name = fullname
#         print("adding a new student in database...")
        
# s1 = Student("Shuaib")
# print(s1.name)      

# s2 = Student("Muneer")
# print(s2.name)  
        

#2
# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)    


# #3
# class Studetn2:
#     def __init__(self,name, marks):
#         self.name = name
#         self.marks = marks
     
#     # static method es ko class leval pe leke aa sakh te he 
#     @staticmethod  # this is decorator 
#     # this is normal func
#     def hello():
#         print("hello")    
        
        
#     def get_avg(self):
#             sum = 0
#             for val in self.marks:
#                 sum += val
#             print("hi", self.name, "your avg score is:", sum/3)    
                
# s2 = Studetn2("Tony stark", [99, 98, 97])
# s2.get_avg()

# # second object call
# s2.name = "Shuaib"
# s2.get_avg()

# #third object call
# s2.name = "muneer"
# s2.get_avg()
# s2.hello()
    
    
    #1 Important 
    #Abstraction es ka matlab hota he koi chease chopana 
    
    #Hiing the implementtation details of a class and only showign the essentail features to  the user.
    
    # this class create 
    

# class Car:
#     #unasesery chease dikhai our unnasesery chease chupai
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clu = False
        
    
#     def start(self):
#         #unnasesery tesps
#         self.clu = True
#         self.acc = True
#         print("one car started")
        
# # es me ue ho raha he , unnasesery chease chopai, our nasesery chease dikhai. ue hota he abstraction ka matalb hota he           

# car1 = Car()
# car1.start()  

# # second exmple

# class Car2:
#    # this is cart define
#     def __init__(self):
#         self.accc = False
#         self.brkk = False
#         self.cluu = False
        
#     # second method creat
    
#     def srart(self):
#         self.cluu = True # ue unnasesery chease ko kesy use kia. 
#         self.accc = True # ue jo unnasesery chease hou to height hoahi , our nasesery chease creat execc hoahi 
#         print("tow car started....")
# # jo class ke baher unnasesery chease print nahi hoi dekhai nahi de rahy he 
# car3 = Car2()
# car3.srart()        
            
        
              
              
#2 Encapsulation
#Wrapping data and functions into a single unit (object)


# ATm 

# class Atm:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
    

# # this is object 
# atm = Atm(100000, 12345)
# print(atm.balance)
# print(atm.account_no)        


# # Atm simple project
# class Atm2:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
        
#     # creat a debit method 
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("Total balance=", self.get_balance())
    
    
#     # creat a method
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credit")
#         print("Total balance =", self.get_balance())
    
    
#     def get_balance(self):
#         return self.balance

# # this is object 
# atm = Atm2(10000, 12345)
# atm.debit(1000)
# atm.credit(500)



# # delete method 
# class Studetn3:
#     def __init__(self, name):
#         self.name = name
        
# s4 = Studetn3("Suaib")
# print(s4.name)     
# del s4   
# print(s4.name)


# private(like) attributes & methods
# 1 simple exmple
# class Acount3:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass


# acount = Acount3("12345", "abcde")

# print(acount.acc_no)
# print(acount.acc_pass)

        
  # 2 private exmple
  
# class Student4:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass # this argiument private acc_pass 
        

# stu = Student4("12345", "abcde")
# print(stu.acc_no, stu.__acc_pass) # end acc_pass private              


# 3 exmple

# class Studetn5:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
    
#     # second method reset passworld
#     def reset(self):
#         print(self.__acc_pass ) 
        
# # this is object 
# abc = Studetn5("12345", "abcde")
# print(abc.acc_no)           

# # ths is change in method reset call
# print(abc.reset())

# this is private class
# class Person:
#     __name = "anonymous"
    
#     def __hello(self):
#         print("hello person")
    
#     # second method 
#     def  welcome(self):
#         self.__hello() 
# p = Person()
# print(p.welcome())        
    
# class One:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
        
#     def age1(self):
#         print(self.__age)    
#     def __one(self):
#         print("hello this is me shuaib")
#     # this is second method 
#     def welcome(self):
#         print(self.__one())
# o = One("Shuaib", 23)
# print(o.welcome())      
# print(o.name)  
# print(o.age1())
    


# class Muneer:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass  = acc_pass
        
#     def min(self): 
#         print(self.__acc_pass)  


# m = Muneer("12345", "abcde")
# print(m.acc_no)
# print(m.min())


# class Atm2:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
        
#     # creat a debit method 
#     def debit(self, prise):
#         self.balance -= prise
#         print("Rs.", prise, "was debited", )
#         print(f"Total Amount, {self.get_balance}", )
    
    
#     # creat a method
#     def credit(self, prise):
#         self.balance += prise
#         print("Rs.", prise, "was credit")
#         print(f"Total Amount, {self.get_balance()}")
    
    
#     def get_balance(self):
#         return self.balance

# # this is object 
# atm = Atm2(100000, 12345)
# atm.debit(1000)
# atm.credit(500)


# this is single perince class

# class Car:
#     color = "blue"
#     @staticmethod
#     def start():
#         print("car started....")
#     @staticmethod
#     def stop():
#         print("cart stoped...")

# this is single child class 
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar ("prius")
# print(car1.start()) 
# print(car1.color)   

    
# # Inheretnce simple practice
# class A:
#     @staticmethod
#     def B():
#         print("A")
    
#     def C():
#         print("C")

# and single child class
# class AB(A):
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
        
#     def about(self):
#             return(f"Name:{self.name}\nAge:{self.age}\nCity:{self.city}")
# to create a object 
# ab = AB("Shuaib", 22, "Karachi")
# and call method 
# print(ab.about())

# this is practice inheritence 
# this is single perince class
# class Car:
#     @staticmethod
#     def start():
#         print("Car started....")
    
#     @staticmethod
#     def stop():
#         print("Car stoped....")
    
# # this is single child class   
# class CartToyota(Car):
#     def __init__(self, brand,):
#         self.brand = brand
             

# # this is multipal child class
# class Fortuner(CartToyota):
#     def __init__(self, type):
#         self.type = type
# car1 = Fortuner("diesel")
# car1.start()        

        
                
# class A:
#     varA = "welcome to class A" 
# class B:
#     varB = "welcome to class B"
# class C(A, B):
#     varC = "welcome to class C" 
# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)           
                          


# Supeer method practice 


# class Car:
#     def __init__(self, type, ):
#         self.type = type
        
        
#     @staticmethod
#     def start():
#         print("Car stared...")
    
#     @staticmethod
#     def stop():
#         print("car stop")
    
#     @staticmethod
#     def about():
#         print(f"Name")    
        
# class ToyotaCar(Car):
#     def __init__(self, name, type):
#      super().__init__(type)
#      self.name = name
#      super().start()
#      super().stop()
#      super().about()
        
        
# car1 = ToyotaCar( "" , "eletric" )
# print(car1.type)        



# Encapsulation  overloading

# # overloding
# class Point:
#   name = "shuaib"
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

#   #overloading
#   def __add__(self, other):
#     return Point(self.x * other.x, self.y * other.y)
    
  
#   def __str__(self):
#     return f"Point({self.x}, {self.y})"

# point1 = Point(1,2)
# point2 = Point(3,4)

# point3 = point1 + point2
# print(point3)



# Class varaiable this is common all class and method

# #  class variable ex:
# class Student:
#   school_name = " ABC HIGH Scholl" # class variabl
#   def __init__(self, name , grade): # this constructor
#     self.name = name  
#     self.grede = grade
#   def show(self):
#     print(f"Name:{self.name}\nGrade:{self.grede}\nSchool:{self.school_name} \n")

# # creat a object
# st1 = Student(" shuaib ",  " 5th ")

# st2 = Student(" Muneer ", " 6th ")

# # call
# st1.show()
# print("...........\n")
# st2.show()



