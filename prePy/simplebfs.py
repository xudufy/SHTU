s=str(input('yeahyeahn&m:'))
a=s.split(' ')
n=int(a[0])
m=int(a[1])
a[:]=[]
for i in range(0,n):
    line=[]
    for j in range(0,m):
        line.append(False)
    a.append(line)
print(a)
