L1=[24,'a',"python",46.5,'true']
print(L1)
print(L1[0])
print(L1[2])
print(L1[0:3])
print(L1[2:4]) #add any eliments append()
L1.append("cse209")#yadi kuchh bhi add karna ho list me to append ka use kiya jata hai
print(L1)
L1.insert(2,"INT108")#ydi position ke sath kisi elimant ko insert karna hai to insert ka use karenge 
print(L1)
print(L1[2])

# extend karne ke liye L1.extend(L2) ka use karenge
#append () add any element to the end of the list
#insert() to add an element at any place
#extend () or concatenation
L2=[15,'b',"java",23.76,'false']
L3=L1+L2
print(L3)
T1=('a','b','c') #TUPLES
print(T1)
print(T1[0:2])
print(list(T1)) # ye wala [] is braket me aa jayega 