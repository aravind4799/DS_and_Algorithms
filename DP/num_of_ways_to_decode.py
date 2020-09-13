# a->1 ....z->26 to find number of ways to decode 226
# 2->b 2->b 6->f  --+1
# 22->v 6->f      --+1
# 2->b 26->z      --+1
# ans:3

n=input("enter string to decode: ")
def helper(s,k,memo):
    if k==0:
        return 1
    start=len(s)-k
    if s[start]=='0':
        return 0
    if memo[k]!=None:
        return memo[k]
    result=helper(s,k-1,memo)
    if k>=2 and int(s[start:start+2])<=26:
        result+=helper(s,k-2,memo)
    memo[k]=result
    return result

memo=[None for _ in range(len(n)+1)]
print(helper(n,len(n),memo))
    
