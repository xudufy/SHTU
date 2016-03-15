def nSum(s,step=1):
    ans=0

    if step<len(s):
        lmax=step
    else:
        lmax=len(s)

    for i in range(lmax):
        ans+=int(s[i])

    if step>=len(s):
        return ans
    else:
        return ans+nSum(s[step:],step)

s=input()
print(nSum(s,1))
print(nSum(s,8))
