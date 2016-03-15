a=int(input())
s=str('')
s1=str('')
while a!=-1:
    k=1
    maybe,maybe2=0,0
    for i in range(1,9):
        maybe+=(a%10)*k
        maybe2+=(1-(a%10))*k
        k=k*2
        a=a//10
    s+=chr(maybe)
    #s1+=chr(maybe2)
    a=int(input())
print(s)
#print(s1)
