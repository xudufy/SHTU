num=[]
def calc(s):
    global num
    for i in s.split():
        try:num.append(int(i))
        except:
            if i in ['+','-','*','/']:
                a=num.pop()
                if i=='+':num[-1]+=a
                elif i=='-':num[-1]-=a
                elif i=='*':num[-1]*=a
                else:num[-1]//=a
    try:
        return num[0]
    except:
        pass

if __name__=='__main__':
    while True:
        try:s=str(input())
        except:break
        calc(s)
    print(num[0])
    exit()
