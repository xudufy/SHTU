s=str(input())
a=[]
for i in s:
    a.append(int(ord(i)-96 if i>'a' else ord(i)-48))
b=[]
for k in range(0,len(a)//2):
    b.append(a[2*k]*16+a[2*k+1]+48)
print(b,sep='')
