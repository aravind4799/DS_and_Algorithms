#find to number of palindromes that can be formed from a string
#brute force: to find all substring and to check if each substring is a palindrome
#would take o(n*3)


s=input()
ans=0
#count number of odd palindrome
#treat every element as a middle element and check left and right of it
l=len(s)
for i in range(l):
    j=0
    while(i-j>=0 and i+j<l):
        if s[i-j]==s[i+j]:
            ans+=1
        else:
            break
        j+=1
    
#to find even length palindromes we need to compare adjacents
for i in range(l):
    j=0
    while(i-j>=0 and i+j+1<l):
        if s[i-j]==s[i+j+1]:
            ans+=1
        else:
            break
        j+=1

print("number of palindrome_decomposition possible for given string:{}".format(ans))

