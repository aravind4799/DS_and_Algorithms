#segmented seive is used to find prime in range when n is of order 10**12 or more


from time import time
import math

def seive(limit):
    start=time()
    prime=[True]*limit
    prime[0],prime[1]=False,False
    prime_no=[]
    p=2
    while(p*p<limit):
        for j in range(p*p,limit,p):
            prime[j]=False
        p+=1
        
        if(p*p<limit and not prime[p*p]):
            p+=1
    for i,j in enumerate(prime):
        if j:
            prime_no.append(i)
    end=time()
    return prime_no

def print_prime_in_range(low,high):
    prime=seive(math.ceil(math.sqrt(high)))
    prime_no=[True]*(high-low+1)
    #now iterate prime and strict out all the multiples of prime
    for p in prime:
        #find the base ..just that it is smaller or equal to l
        base=(low//p)*p
        if base<low:
            base+=p

        for i in range(base,high+1,p):
            prime_no[i-low]=False
        if base==0:#means low number is a prime
            prime_no[base]=True
    ans=[]
    for i,j in enumerate(prime_no):
        if j:
            ans.append(i+low)

    return ans

print(print_prime_in_range(900,1000))





     