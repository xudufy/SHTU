#global varibles
oprt=['+','-','*','/']
num=[]

def check(st):
    s=''
    for i in range(0,len(st)):
        if st[i] in ['\t','\r','\n',' '] and i!=0 and not(st[i-1] in ['\t','\r','\n',' ']):
            s+=' '
        elif not(st[i] in ['\t','\r','\n',' ']):
            s+=st[i]
    s+=' '
    return s

def calc(s):
    temp1=0;
    for i in range(0,len(s)):
        if ord(s[i])-48 in range(0,10):
            if s[i-1] == '-':
                temp1=0-int(s[i])
            else:
                temp1=temp1*10+int(s[i])
        elif s[i]==' ':
            if s[i-1]=='+':
                a=num.pop()
                num[-1]+=a
            elif s[i-1]=='-':
                a=num.pop()
                num[-1]-=a
            elif s[i-1]=='*':
                a=num.pop()
                num[-1]*=a
            elif s[i-1]=='/':
                a=num.pop()
                num[-1]//=a
            elif ord(s[i-1])-48 in range(0,10):
                num.append(temp1)
                temp1=0
# main
while True:
    try:
        s=str(input())
    except:
        break
    calc(check(s))
print(num[0])
exit()
