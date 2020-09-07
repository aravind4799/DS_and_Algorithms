#finding gcd by euclids
# gcd(a,b)=gcd(b,a%b) untill b==0 note a>b
def gcd(a,b):
    flag=1
    if b>a and flag:
        a,b=b,a
        flag=0
    if b==0:
        return a
    return gcd(b,a%b)

# def gcd(a,b):
#     minn = a if a<b else b
#     while(minn>=1):
#         if a%minn==0 and b%minn==0:
#             return minn
#         minn-=1

def lcm(a,b):
    return int(a*b/gcd(a,b))

# finding hcf and lcm of array

arr=[16,48,2,4,8,117]
from functools import reduce

print(reduce(gcd,arr))
print(reduce(lcm,arr))



