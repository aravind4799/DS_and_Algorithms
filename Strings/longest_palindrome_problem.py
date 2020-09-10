#given a string .print the length of longest palindrome that can be made from that
#string

from collections import Counter

s=input()
d={}
d=Counter(s)
ans=0
odd_freq_found=False
for freq in d.values():
    if freq%2==0:
        ans+=freq
    else:
        odd_freq_found=True
        ans+=freq-1

if odd_freq_found:
    ans+=1

print("length of longest palindrome that can be formed from given string:{}".format(ans))

    