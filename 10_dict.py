#filename:dict.py

d={'michael':95,'bob':75,'tracy':85}
print(d['michael'])

d['bob']=67
print(d['bob'])

if 'zhangchao' in d:
   print('it is impossable')

if d.get('zhangchao',1):
	print('it is impossable')

d.pop('bob')
print(d)

a=[]
a.append(input('enter name:'))
temp=int(input('enter age:'))
a.append(temp)
print(a)
d[a[0]]=a[1]

print(d)
print(d.keys())
print('a[0]:',a[0])

for key in d.keys():
	print(key,'****',a[0])
	if key==a[0]:
         print(a[0],' is exit')


s1=set([1,2,4,34,5,2,56])
print(s1)

s1.add(5)
s1.remove(5)

s2=set([3,5,6,7,8,8,8,8,2])

s3=s1 & s2
s4=s1 | s2

print(s3)
print(s4)

