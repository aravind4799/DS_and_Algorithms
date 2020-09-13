# given a array and value need to return number of subsets possible which
# add up to given value in the array
# eg:[2,4,6,10] and 16
# ans:2 -> [6,10],[4,2,10]

a=list(map(int,input().split()))
v=int(input("enter subset sum value:"))

def helper(a,total,i,mem):
    key=str(total)+":"+str(i)
    if key in mem:
        return mem[key]
    if total==0:
        return 1
    elif total<0:
        return 0
    elif i<0:
        return 0
    if a[i]>total:
        result=helper(a,total,i-1,mem)
    else:
        result=helper(a,total,i-1,mem)+helper(a,total-a[i],i-1,mem)
    mem[key]=result
    return result

mem={}
print(helper(a,v,len(a)-1,mem))
