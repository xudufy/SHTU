n=int(input('number:'))
a=[True,True]
for i in range(2,n):
    a.append(True)
for i in range(2,n):
    if a[i]:
        j=2
        while j*i<=n-1:
            a[i*j]=False
            j+=1
        print(i,end=' ')
print()
