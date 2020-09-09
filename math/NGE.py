# Given an array, print the Next Greater Element (NGE) for every element.
# The Next greater Element for an element x is the first greater element
# on the right side of x in array.Elements for which no greater element 
# exist, consider next greater element as -1.

# numbers = list(map(int,input().split()))

# for i in range(len(numbers)):
#     dumm=-1
#     for j in range(i+1,len(numbers)):
#         if numbers[i]<numbers[j]:
#             dumm=numbers[j]
#             break
#     print(dumm,end=" ")



def isempty(stack):
    return len(stack)==0

def printarr(arr):
    stack=[]
    ele=0
    nextt=0
    stack.push(arr[0])

    for i in range(1,len(arr)):
        nextt=arr[i]

        if(not isempty(stack)):
            ele=stack.pop()

            while(ele<nextt):
                print(str(ele)+"--"+str(nextt))
                if(isempty(stack)):
                    break
                ele=stack.pop()
        
        if(ele>next):
            stack.push(ele)
        
        stack.push(nextt)



    


    

    





