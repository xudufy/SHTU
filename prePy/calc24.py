#models:
#0:((1+2)+3)+4
#1:(1+2)+(3+4)
#2:1+(2+3)+4
#3:1+((2+3)+4)
#4:1+(2+(3+4))

def __init__():
    global numList,numUsed,nums,numberOfAnswers,leftBracketPosition,rightBracketPosition
    global operators,operatorList,alreadyFindAnswer,answers,find_all,oprtPrior,oprt
    oprtPrior={
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '^':3,
    }
    oprt=('+','-','*','/','^','(',')')
    find_all=True
    answers=''
    numList=[]
    numUsed=[False,False,False,False]
    nums=[]
    leftBracketPosition=((2,0,0,0,0),(1,0,1,0,0),(0,1,0,0,0),(0,2,0,0,0),(0,1,1,0,0))
    rightBracketPosition=((0,0,1,1,0),(0,0,1,0,1),(0,0,0,1,0),(0,0,0,1,1),(0,0,0,0,2))
    operators=('+','-','*','/')
    operatorList=[]
    alreadyFindAnswer=False
    numberOfAnswers=0

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

def init(s):
    global find_all
    for i in s.split():
        try:
            nums.append(int(i))
        except:
            print(i)
            if i.upper=="FALSE":
                 find_all=False
    return True if len(nums)==4 else False;

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
    return num[0]

def output(a):
    return int(a) if abs(int(a)-a)<=0.00001 else a

def evalMidE(s):
    return output(postToAns(midToPost(initSplit(s))))

def check():
    global operatorList
    global numList
    global alreadyFindAnswer,find_all
    global numberOfAnswers
    global answers
    for i in range(5):
        s=''
        s+='('*leftBracketPosition[i][0]
        s+=str(numList[0])
        s+=')'*rightBracketPosition[i][1]
        for j in range(1,4):
            s+=operatorList[j-1]
            s+='('*leftBracketPosition[i][j]
            s+=str(numList[j])
            s+=')'*rightBracketPosition[i][j+1]
        try:
            answer=float(evalMidE(s))
        except:
            pass
        else:
            if answer<24.0001 and answer>23.9999:
                answers+=s+'\n'
                numberOfAnswers+=1
                alreadyFindAnswer=True
                return

def workOP():
    global operatorList
    global numList
    global alreadyFindAnswer,find_all
    for i in range(4):
        for j in range(4):
            for k in range(4):
                operatorList=[operators[i],operators[j],operators[k]]
                check()
                numList[0]=-numList[0]
                check()
                numList[0]=-numList[0]
                if not(find_all) and alreadyFindAnswer:
                    return

def workNum(level):
    global operatorList
    global numList
    global alreadyFindAnswer,find_all
    global nums
    global numUsed
    if not(find_all) and alreadyFindAnswer:
        pass
    elif level<=4:
        for i in range(4):
            if not numUsed[i]:
                numUsed[i]=True
                numList.append(nums[i])
                if level==3:
                    workOP()
                else:
                    workNum(level+1)
                if  not(find_all) and alreadyFindAnswer:
                    return
                numList.pop()
                numUsed[i]=False

def calc24(temp_nums,find_all_d=True):
    global numList,numUsed,nums,numberOfAnswers,leftBracketPosition,rightBracketPosition
    global operators,operatorList,alreadyFindAnswer,answers,find_all
    __init__()
    find_all=find_all_d
    nums=list(temp_nums)
    workNum(0)
    if find_all:
        answers+='{0} answers have been found!'.format('No' if numberOfAnswers==0 else numberOfAnswers)
    return answers[:len(answers)-1] if answers[-1:]=="\n" else answers;

if __name__=="__main__":
    __init__()
    inputString=''
    inputString=str(input('4 numbers:'))+"\n"
    while not(init(inputString)):
        inputString=str(input(''))+"\n"
    print(calc24(nums,False))
