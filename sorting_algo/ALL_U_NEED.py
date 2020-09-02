from random import randint
def create_array():
    return [randint(0,50) for i in range(10) ]

def insertion_sort(a):
    #pick up a number and place it its sorted position in the current window
    for index in range(1,len(a)):
        insert_elem=a[index]
        insert_index=index

        while(insert_index>0 and a[insert_index-1]>insert_elem):
            a[insert_index]=a[insert_index-1]
            insert_index-=1

        a[insert_index]=insert_elem
    return a


def bubble_sort(a):
    #at each iteration the largest element gets to accumated towards the end
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
        # print(a)
        #at every iteration reduce the window from left direction
    return a

def selection_sort(a):
    # at every iteration the array gets sorted from the front side,reverse of the 
    #bubble sort
    for i in range(len(a)):

        min_index=i

        for j in range(i,len(a)):
            if a[j]<a[min_index]:
                min_index=j
        #at the end of j loop we get minimum element in the array at index min_index

        a[i],a[min_index]=a[min_index],a[i]
        print(a)
        #at every iteration next smallest element comes to first
        #swap the ith and smallest element
        #at every iteration the reduce the window length from right 
    return a

def merge(a,b):
    #a and b are sorted array we need to form a sorted array from these
    i,j=0,0
    sorted_array=[]
    while(i<len(a) and j<len(b)):
        if a[i]<b[j]:
            sorted_array.append(a[i])
            i+=1
        else:
            sorted_array.append(b[j])
            j+=1       
    if i==len(a):
        #if array a is exhausted add remaining elements of b
        sorted_array.extend(b[j:])
    else:
        #if array b is exhausted add remaining elements of a 
        sorted_array.extend(a[i:])
    return sorted_array

def merge_sort(a):
    if len(a)==1:
        return a
    #basic idea behind merge_sort is to take advantage of sorting two sorted array
    left,right=merge_sort(a[:len(a)//2]),merge_sort(a[len(a)//2:])
    return merge(left,right)


def quick_sort(a):
    if len(a)<=1:
        return a
    smaller,larger,equal=[],[],[]

    pivot=a[randint(0,len(a)-1)]
    print(pivot)

    for x in a:
        if x<pivot: smaller.append(x)
        elif x==pivot: equal.append(x)
        else: larger.append(x)
    
    return quick_sort(smaller)+equal+quick_sort(larger)

a=[5,4,3,2,1]
print(a)
print(quick_sort(a))
            





        


    