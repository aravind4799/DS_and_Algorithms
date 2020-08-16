a=[1,2,3,4,5]
def left_rotation(a,k):
    k=k%len(a)
    return a[k:]+a[:k]

def right_rotation(a,k):
    k=k%len(a)
    return a[-k:]+a[:-k]

print(right_rotation(a,2))