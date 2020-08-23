n=int(input())
#naive recursive sol
#complexity is o(2*n)
# def fibo(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
#o(n)
def fibo(n):
    if n==1 or n==2:
        return n
    dp_arr=[0]*int(n+1)
    dp_arr[0]=1
    dp_arr[1]=1
    for i in range(2,n):
        dp_arr[i] = dp_arr[i-1] + dp_arr[i-2]
    return dp_arr[n-1]
print(fibo(n))


