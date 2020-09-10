#two strings are called anagrams to each other if they can be rearranged in some 
#way to get the other string,, in other words they should have same letter frequency
# example
# aravind and draaivnd are anagrams
from collections import Counter
string1=input()
string2=input()
def anagram(a,b):
    if(len(a)==len(b) and Counter(a)-Counter(b)=={}):
        return True
    else:
        return False
print(anagram(string1,string2))
