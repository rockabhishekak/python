# class Demo:
#     pass
# D1=Demo()
# print(D1)
#how to creat a class

# class myfirstprog:
#     print("welcome to object oriented programming")
# c=myfirstprog()
# print(c)

# class Rectangle:
#     lenght=9 #attribute lenght
#     width=5#attribute width
# R1 = Rectangle() # object of a class
# print(Rectangle.lenght) #access attribute lenght
# print(R1.width)# access attribute width

#self parameter 
# class Methoddemo:
#     def Display_message(self): ##This is method defind 
#         print("Abhishek")
# ob1=Methoddemo()
# ob1.Display_message()

# class Circle:
#     def Circle_area(self,radius):
#         return 3.14*radius**2
# ob2=Circle()
# print(ob2.Circle_area(5))

# class Rectangle:
#     def Area_of_rectangle(Self,lenght,width):
#         return lenght*width
# ob3=Rectangle()
# print(ob3.Area_of_rectangle(5,3))

# class Grater:
#     def gt(self,a,b):
#         if a>b:
#             k=a
#             print("Number",a,"is Greater")
#         else:
#             k=b
#             print("Number",b,"is Greater")
#         self.ev(k)
#     def ev(self,c):
#         if c%2==0:
#             print("Number",c,"is Even")
#         else:
#             print("Number",c,"is Odd")
# a=int(input("Enter your 1st number: "))
# b=int(input("Enter your 2nd number: "))
# ob=Grater()
# ob.gt(a,b)


# class practice:
#     x=5
#     def display(self,x):
#         x=30
#         print(x)
#         print(self.x)
# ob=practice()
# ob.display(50)

# class Self_demo:
#     def method_a(self):
#         print("now in method a")
#         print("i am method a")
#     def method_b(self):
#         print("in method b calling method a ")
# a=Self_demo()
# a.method_b()




# class Self_demo:
#     def method_a(self,a):
#         print("now in method a")
#         print("i am method a")
#     def method_b(self):
#         print("in method b calling method a")
#         self.method_a(a) #calling method_a
# a=Self_demo()
# a.method_b()


# print(dir(Self_demo))#know attribute

# class Person:
#     def __init__(self):
#         self.name = "Abhishek" #public attribute
#         self.__bankaccno=1548874545845  #private attribute
#     def Display(self):
#         print("name is:",self.name)
#         print("bank acc no.:",self.__bankaccno)
# p=Person()
# print(p.name)
# # p.Display()
# # print(p.__backaccno)
# print(p._Person__bankaccno)
# # p.Display

# class Circle:
#     pi = 0
#     radius = 0
#     def __init__(self):
#         self.pi=3.14
#         self.radius=5
#     def calc_area(self):
#         print(self.radius)
#         return self.pi*self.radius**2
# c1=Circle()
# print(c1.calc_area)

# class box:
#     width=0
#     height=0
#     depth=0
#     valume=0
#     def __init__(self):
#         self.width=55
#         self.height=5
#         self.depth=5
#         print(self.width*self.height*self.depth)
#     def vol(self):
#         print("Width: ",self.width)
#         print("Height: ",self.height)
#         print("Depth: ",self.depth)
#         return self.width*self.height*self.depth
# b1=box()
# print("volume of cube is = ",b1.vol())


# 1 WAP to cheak whether nummber is prime or not

# # To take input from the user
# class prime:
#     num = int(input())

#     if num > 1:
    
#         for i in range(2, (num//2)+1):
#             if (num % i) == 0:
#                 print(num, "is not a prime number")
#                 break
#         else:
#             print(num, "is a prime number")
#     else:
#         print(num, "is not a prime number")
# d=prime()

#2.WAP to a cheak number is armstrong or not 
# class armstrong:
#     num = int(input("Enter a number: "))
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10

#     if num == sum:
#         print(num,"is an Armstrong number")
#     else:
#         print(num,"is not an Armstrong number")
# od=armstrong()

#3 WAP to cheak palindrame or not 
class pal:
    def palindrom(self):
        a=int(input())
        reverse=a[::-1]
        if (reverse==0):
            print("palidrome")
        else:
            print("not palidrome")
d=pal()
d.palindrom()