import numpy as np
# Count the number of inversions in an array

arr = [2, 4, 1, 3, 5]


# Slow solution

def count_inversions(arr):
    inv = 0
    for i in range(0, len(arr)):
        for j in range (i, len(arr)):
            if (arr[j] > arr[i]):
                inv+=1
    
    return inv
    
total_inversions = 0
def mergesort(arr):
    global total_inversions
    high = len(arr)
    low = 0
    mid = (high - low)/2
    
    if len(arr) == 1:
        return arr
    else:
        a1 = mergesort(arr[:mid])
        a2 = mergesort(arr[mid:])
        return merge(a1, a2)
    

def merge (arr1, arr2):
    global total_inversions
    i1, i2, oi = 0, 0, 0
    out = np.zeros(len(arr1) + len(arr2))
    while(i1 < len(arr1) and i2 < len(arr2)):
        if(arr1[i1] <= arr2[i2]):
            out[oi] = arr1[i1]
            oi+=1
            i1+=1
        else:
            total_inversions+= (len(arr1) - i1)
            out[oi] = arr2[i2]
            oi+=1
            i2+=1
    
    while i1 < len(arr1):
        out[oi] = arr1[i1]
        i1+=1
        oi+=1
    while i2 < len(arr2):
        out[oi] = arr2[i2]
        i2+=1
        oi+=1
    
    return out

    
print mergesort(arr)
print total_inversions