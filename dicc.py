# d1 = {}
# print(type(d1))

# d = {"K24CN":30,"Abhishek":32}
# print(d)
# d2={}
# d2['name']='Abhishek'
# d2['age']=20
# print(d2)
# d3 = dict(name='abhishek')
# print(d3)

# a=dict([('name','abhishek'),('age',19)])
# print(a)
# b=dict([('name',['abhishek','hello']),('age',20)])
# print(b)
# A={'I':'India','A':'America'}
# B={'I':'Italy','A':'America'}
# print(A==B)
# print(A!=B)
# C=A
# print(C)
# print(C==A)
# asicode={'A':65,'B':66,'C':67,'D':68}
# print(asicode.keys())
# print(asicode.values())
# print(asicode.items())
# # print(asicode.clear())#delet all items
# print(asicode)
# print(asicode.get('C'))#return the values of key
# print(asicode.pop('B'))#remove the key & return value


#traversing dictionaries
grades={'ram':'A','sham':'B','abhishek':'C'}
for key in grades:
    print(key,':'(grades[key]))