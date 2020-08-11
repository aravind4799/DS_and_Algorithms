# given a string,
# reverse it and find which chars remains in same position as original

n=str(input("enter a string:"))
count=0

for i in range(len(n)):
    if n[i]==n[::-1][i]:
        count+=1
print(count)