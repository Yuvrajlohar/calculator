# # list

# # a1= [1,2,3,4,1,1,1,1,1,1,]
# # a,b,c,d= set(a1)

# # print(a)


# #method two 
# # a1= [1,2,3,4,1]
# # a,b,c,d = a1


# # a= {758468 : "s"}
#     # 1 : "v",
#     # 1 : "hal"}

# # print(a[1])


# # Python program to demonstrate instantiating
# # a class
# class Dog:

#     # A simple class attribute
#     attr1 = "mamal"
#     attr2 = "dog"

#     # A sample method
#     def fun(ab):
#         print("I'm a", ab.attr1)
#         print("I'm a", ab.attr2)
        
#     def greet(ab):
#       print("hope you are doing well")


# # Driver code
# # Object instantiation
# Rodger = Dog()

# # Accessing class attributes and method through objects
# print(Rodger.attr1)
# print(Rodger.attr2)
# Rodger.fun()
# Rodger.greet()


# class uv:
#     def _init_(self,name,age):
#         self.name=name
#         self.age = age

#     def show(self):
#         print("hello{self.name},{self.age}")

# s1= uv("yuvraj",45)
# s1.show()

# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
    
#     def display_details(self):
#         print(f"Name:{self.name}")
#         print(f"rollno:{self.rollno}")
#         print(f"marks:{self.marks}")
#     def grades(self):
#         if (self.marks>=90):
#             print("A")
#         elif(76<=self.marks<90):
#             print("B")
#         elif(60<=self.marks<75):
#             print("C")
#         elif(35<=self.marks<60):
#             print("D")
#         else:
#             print("fail")
        

# student1=Student("yuvraj",11,55)
# student2=Student("vishu",24,59)

# student1.display_details()
# print(f"Grade of student",student1.grades())

#Q  creating class for bankaccount with deposit and withdraw methods.memoryview
# class bankaccount:
#     def __init__(self,name,balance=0):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.amount=amount
#         self.balance=self.balance+amount
#         print(f"your current balance is{self.balance}")


# class ram:
#     print("hh")
#     __a=12
#     __a=15
#     # b=__a
#     print(b)
#     def __ritendra():
#         id=3


#     def __fun():
#         id=2
#         print(ram.__a)
#     # def f2():
#     #     ram.fun()

# ram.fun()

# # ram.f2() 


# class bankdetails:
#     def __init__(bankdetails,name,id,age,password):
#         bankdetails.__new(name,id,age,password)

#     def __new(bankdetails,name,id,age,password):
#         bankdetails.name=name
#         bankdetails.id= id
#         bankdetails.age=age
#         bankdetails.password=password
#         print("hello",bankdetails.name)
#     def yuvraj(bankdetails):
#         a = str(input("entre your pass"))
#         if(a==bankdetails.password):
#             print(bankdetails.name,"\n",bankdetails.id,"\n",bankdetails.age)
#         else:
#             print("you are someone else")    
    
    
    
# b= bankdetails("yuvraj",5,55,"Yuvraj")
# print(b.yuvraj())




class Book:
    def __init__(Book,author,title):
        Book.author=author
        Book.title=title
    def show_info(Book):
        
        print(Book.author,Book.title)
    
# Book("Yuvraj","my name ")
# Book.show_info()

a = Book("he","me")
a.show_info()
        

            


        