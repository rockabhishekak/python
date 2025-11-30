'''file heander'''

# f=open('K24CN.txt','r')
# # str=f.read()
# str=f.read(4)
# print(str)
# f.close()

'''---file store a grops of data----- '''

# f=open('K24CN.txt','w')
# print('enter text(@ at end):')
# while True:
#     text=input()
#     if text=='@':
#         break
#     f.write(text + '\n')
# f.close()

'''----file read--- '''
# f=open('K24CN.txt','r')
# text=f.read()
# print(text)
# f.close()

'''-----file seek-----'''
# f=open("K24CN",'a+')
# print('enter text to append (@ st end):')
# while True:
#     str=input()
#     if str=='@':
#         break
#     else:
#         f.write(str + '\n')
# f.seek(0,0)
# print('the file contents are: ')
# str=f.read()
# print(str)
# f.close()

# import os,sys
# filename=input('enter the file name:')
# if  os.path.isfile(filename):
#     f=open(filename,'r')
# else:
#     print(filename,'does not exist')
#     sys.exit()
# print('the file contents are:')
# str=f.read()
# print(str)
# f.close

'''< -----file line count----->'''

# f=open('K24CN.txt','r')
# count=0
# for line in f:
#     count=count+1
# print('the number of lines are:',count)
# f.close
# '''---file charater count---'''

# f=open('K24CN.txt','r')
# count=0
# for line in f:
#     if line[-1]=='\n':
#         line=line[:-1]
#     count=count+len(line)
# print('the number of charaters are:',count)
# f.close
# '''----file word count----'''

# f=open('K24CN.txt','r') 
# count=0
# for line in f:
#     words=line.split()
#     count=count+len(words)
# print('the number of words are:',count)
# f.close()


# import os,sys
# filename=input('enter the file name:')
# if  os.path.isfile(filename):
#     f=open(filename,'r')
# else:
#     print(filename,'does not exist')
#     sys.exit()

#     cl=cw=cc=0
#     for line in f:
#         words=line.split()
#         cl += 1
#         cw += len(words)
#         cc += len(line)
#     print('the number of lines are:',cl)    
#     print('the number of words are:',cw)
#     print('the number of charaters are:',cc)
# print('the file contents are:')
# str=f.read()
# print(str)
# f.close()

'''---file hidden----'''

# import pickle
# f=open('abhiishek.txt','wb')
# n=int(input('how many employees:'))
# for i in range(n):
#     id =int(input('enter id:'))
#     name=input('enter name:')
#     sal=float(input('enter salary:'))
#     pickle.dump(id,f)
#     pickle.dump(name,f)
#     pickle.dump(sal,f)
# f.close()
'''<-----file read---->'''
import pickle
f=open('abhiishek.txt','rb')
print('employee details:')
while True:
    try:
        obj=pickle.load(f)
        print(obj)
       
    except EOFError:
        print('end of file reached')
        break
f.close()