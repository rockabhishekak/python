# class test:
#     a=0
#     b=0
#     def __init__(self,x,y):
#         self.a=x
#         self.b=y
#     def equal(self,abc):
#         if(abc.a==self.a and abc.b==self.b):
#             return True
#         else:
#             return False 
# ob1=test(10,20)
# ob2=test(10,20)
# ob3=test(12,90)
# print('ob1==obj2',ob1.equal(ob2))
# print('obj1==obj3',ob1.equal(ob3))   

# class rect:
#     lenght=0
#     breath=0
#     def __init__(self,l,w):
#         self.lenght=l
#         self.breath=w
#     def area(self,obj):
#         print('lenght',obj.lenght)
#         print('breath',obj.breath)
#         return obj.lenght*obj.breath
# ob1=rect(10,20)
# print('the area of rectangle= ',ob1.area(ob1))
# __del___ (destructor method)
# class demo:
#     def __init__(self):
#         print("welcome")
#     def __del__(self):
#         print('destructor executed successfully')
# ob1=demo()
# ob2=ob1
# ob3=ob1
# print('id of ob1',id(ob1))
# print('id of ob2',id(ob2))
# print('id of ob3',id(ob3))
# del ob1
# del ob2
# # del ob3
# print('id of ob1',id(ob1))
# print('id of ob2',id(ob2))
# print('id of ob3',id(ob3))

# class overload:
#     def add(self,x,y):
#         print(x+y)
#     def add(self,x,y,z):
#        print(x+y+z)
# ob1=overload()
# # ob1.add(10,20)
# ob1.add(10,20,30)