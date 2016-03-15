import math
n=int(input('Look at you the son of the bitch!:'))
for i in range(2,n):
    for x in range(2,int(math.sqrt(i))+1):
        if i%x==0:
            print(i,'=',x,'*',i//x,end='\t')
            break
    else:print(i,'is','a','prime',end='\t')
