# given: string abc

# print:
# a  a
#   b
# c   c

n = str(input("enter string:"))
print(len(n))

index=0


for i in range(len(n)):
    for j in range(len(n)):
        if i==j or i+j+1==len(n):
            print(n[index],end=" ")
        else:
            print(" ",end=" ")
    print()
    index+=1

    
        