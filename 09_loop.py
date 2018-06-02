#Filename loop.py

names=['michael','bob','tracy']
for name in names:
	print(name)

sum=0
for x in[1,2,3,4,5,6,7,8,9,10]:
	sum=sum+x
print(sum)

list(range(5))

sum=0
n=99
while n>0:
   sum=sum+n
   n=n-2
print(sum)

l=['bart','lisa','adam']
for x in l:
 	print('hello',x)

n=1
while n<=100:
	print('%3d'%n,end=' ')
	if n%20==0:
		print('\n')
	n=n+1
print('end')

n=1
while n<=100:
	if n>10:
		break
	print(n)
	n=n+1
print('end')

n=0
while n<10:
	n=n+1
	if n%2==0:
		continue
	print(n)