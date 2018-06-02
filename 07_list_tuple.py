#!C:\Users\huiqi\AppData\Local\Programs\Python\Python36-32
#Filename:list&tuple.py
#-*- coding:utf-8 -*-

classmate=['michael','bob','tracy']
print(classmate)
print(len(classmate))
print(classmate[0])
print(classmate[1])

print(classmate[-1])
print(classmate[-2])

classmate.append('zhangchao')
print(classmate)
classmate.insert(2,'zhangdingchen')
print(classmate)
classmate.pop()
classmate.pop(0)
print(classmate)

classmate[0]='zhangchao'
print(classmate)

l=['python','java',['asp','php'],'scheme']
print(l[2][0])

classmate=('michael','bob','tracy')
t=(1,2)
print(t)

t=('a','b',['A','B'])
t[2][0]='X'
print(t)