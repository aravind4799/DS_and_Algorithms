#binary
from time import time
import random

def generate_binary(size):
    lst= [random.randint(0,1) for i in range(size)]
    return "".join(str(i) for i in lst )

def binary_value(s):
    start=time()
    l=len(s)
    ans=0
    for i in s:
        if i=="1":
            ans+=pow(2,l-1)
        l-=1
    end=time()
    return ans
    
def simple_way(s):
    start=time()
    ans=int(s,2)
    end=time()
    return ans

string=generate_binary(10)

print(binary_value(string))
print(simple_way(string))