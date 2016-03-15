s=''
al='abcdefghijklmnopqqrstuvwxyz'
n=int(input())
for ii in range(-n+1,n):
    i=abs(ii)
    s=''
    s=al[n-1]
    for j in range(-n+i+2,n-i):
        s+='-'+al[i+abs(j)]
    print(s.center(4*n-1,'-'))
