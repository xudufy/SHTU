import math
s=input('input M,N:')
a=s.split(' ');
m=int(a[0])
n=int(a[1])
max=m if m>n else n
min=n if m==max else m
pr=[]
prcheck=[]
for i in range(0,max+1):
    prcheck.append(False)
now=0
for i in range(2,max+1):
    if not prcheck[i]:
        pr.append(i)
    for j in pr:
        try:
            prcheck[j*i]=True
        except:
            pass
        if i%j==0:
            break
for i in range(0,len(pr)):
    if pr[i]>=min:
        temp=i
        break
for i in pr[temp:]:
    now=now+1
    if now%5==0:
        print(i)
    else:
        print(i,end=' ')
if now%5!=0:
    print('\n',end='')
elif now==0:
    print(0)
