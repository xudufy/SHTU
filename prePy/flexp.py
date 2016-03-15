oprtPrior={
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '^':3,
}
oprt=('+','-','*','/','^','(',')')

def initSplit(s):
    s1=''
    last=''
    for i in range(len(s)):
        if s[i] in (' ',','):
            pass
        elif s[i] in oprt and s[i]!='-':
            s1+=' '+s[i]+' '
            last=s[i]
        elif s[i]=='-' and i!=0 and (last in map(str,range(10)) or last==')'):
            s1+=' '+s[i]+' '
            last=s[i]
        else:
            s1+=s[i]
            last=s[i]
    return s1.split(' ')

def midToPost(explist):
    oprtStack=[]
    ans=[]
    for i in explist:
        try:
            ans.append(float(i))
        except:
            if i in oprtPrior:
                while len(oprtStack)!=0 and oprtStack[-1]!='(' and oprtPrior[oprtStack[-1]]>=oprtPrior[i]:
                    ans.append(oprtStack.pop())
                oprtStack.append(i)
            if i=='(':
                oprtStack.append(i)
            if i==')':
                while oprtStack[-1]!='(':
                    ans.append(oprtStack.pop())
                oprtStack.pop()
    while oprtStack!=[]:
        ans.append(oprtStack.pop())
    return ans

def postToAns(explist):
    num=[]
    for i in explist:
        try:
            num.append(float(i))
        except:
            a=num.pop()
            if i=='+':
                num[-1]+=a
            elif i=='-':
                num[-1]-=a
            elif i=='*':
                num[-1]*=a
            elif i=='/':
                num[-1]/=a
            elif i=='^':
                num[-1]**=a
            else:
                raise
    return num.pop()

def output(a):
    return int(a) if abs(int(a)-a)<=0.00001 else a

def evalMidE(s):
    return output(postToAns(midToPost(initSplit(s))))

if __name__ == '__main__':
    print(evalMidE(input()))
