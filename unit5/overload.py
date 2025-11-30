# class overload:
#  def add(self,a,b):
#     print(a+b)
#  def add(self,a,b,c):
#     print(a+b+c)
# o1=overload()
# # o1.add(100,20)
# o1.add(100,20,10)

# class parent:
#     def setcordinate(self,x,y):
#         self.x=x
#         self.y=y
# class child(parent):
#     def draw(self):
#         print('locate point x1 = ',self.x,'on x axis')
#         print('locate point y1 = ',self.y,'on y axis')
# c=child()
# c.setcordinate(10,20)
# c.draw()

# class a:
#     name=''
#     age=0
# class b(a):
#     height=''
# class c(b):
#     weight=''

#     def read(self):
#         print("enter the following values ")
#         self.name=input("enter name: ")
#         self.age=input("enter age: ")
#         self.height=input("enter height: ")
#         self.weight=input("enter weight:  ")
#     def display(self):
#         print("enter values are as follows")
#         print("name",self.name)
#         print("age",self.age)
#         print("height",self.height)
#         print("weight",self.weight)
# C1=c()
# C1.read()
# C1.display()

# """multipale inheritance"""

# class a:
#     a1=0
# class b:
#     b1=0
# class c(a,b):
#     def read(self):
#         print("enter the following values")
#         # self.a1=input("enter value of")
#         self.a1=input("enter value of a1")
#         self.b1=input("enter value of b1")
#         self.c1=input("enter value of c1")
#     def display(self):
#         print("enter values are as follows")
#         print("a",self.a1)    
#         print("b",self.b1)    

class a:
    i=0
    def dis(self):
        print("i m in super class")
class b(a):
    i=0
    def dis(self):
        print("i m in sub class")
        super().dis()
class c(b):
    i=0
    def dis(self):
        print("abhishek")
        super().dis()
        
d1=c()
d1.dis()    