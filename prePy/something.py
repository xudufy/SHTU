import math
def gcd(n1,n2):
    if n1<n2:
        n1,n2=n2,n1
    while n1%n2!=0:
        n1,n2=n2,n1%n2
    return n2
n=int(input())
b=int(input())
print(gcd(n1=b,n2=n))
