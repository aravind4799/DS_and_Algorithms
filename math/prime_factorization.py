#prime factorization using seive()
#find smallest prime factor(spf) for everynumber using seive()
#and recursively divide the number with this SPF and add to prime list
import math

def smallest_prime_factor(limit):
    spf=[0]*(limit+1)
    spf[1]=1
    #smallest prime factor for every even number is 2
    for j in range(2,limit+1):
        spf[j]=2
    for i in range(3,limit+1,2):
        spf[i]=i
    #for odd.
    for k in range(3,math.ceil(math.sqrt(limit+1)),2):
        if spf[k]==k:
            for j in range(k*k,limit+1,k):
                if spf[j]>k:
                    spf[j]=k
    return spf

def prime_factors_of_number(n):
    spf=smallest_prime_factor(n)
    ans=[]
    while n!=1:
        ans.append(spf[n])
        n=n//spf[n]
    return ans

print(prime_factors_of_number(12246))
#2 3 13 157

