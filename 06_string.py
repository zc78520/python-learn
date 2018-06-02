#!C:\Users\huiqi\AppData\Local\Programs\Python\Python36-32
#Filename:string.py
#-*- coding:utf-8 -*-

print('包含中文的Str')

print(ord('a'))
print(ord('中'))
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587\n')

print('中文'.encode('utf-8'))
print('张丁宸'.encode('utf-8'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('张鼎臣'))

print('hello,%s'%'world')
#print('hello,%s and %s'%（'zhangdingchen','zhangchao')) mistake a blank space
print('hello,%s and %s'%('zhangdingchen','zhangchao'))

print('Hi,%s,you have $%d'%('michael',100000))
print('%2d-%02d'%(3,1))
print('%.2f' % 3.1415926)

print('Age:%s.Gender:%s'%(25,True))
print('growth rate:%d %%'%7)
