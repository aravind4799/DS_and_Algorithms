from functools import reduce

def minn(a,b):
    if a>=b:
        return (b,a)
    else:
        return (a,b)
    
def gcd(a,b):
    A,B=minn(a,b)
    if B%A==0:
        return A
    i=A
    while(i>=1):
        if A%i==0 and B%i==0:
            return i
        i-=1

def lcm(a,b):
    return a*b//gcd(a,b)    



