
arr=list(map(int,input().split()))
length=len(arr)
dp_arr=[None]*length

dp_arr[0]=arr[0]

for i in range(1,length):
    dp_arr[i]=max(arr[i],dp_arr[i-1]+arr[i])

print(max(arr))




