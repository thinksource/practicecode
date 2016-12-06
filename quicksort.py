import random

def swap(a, b):
    return (b, a)

def partition(a, left,right, pivotIndex):
    pivotValue = a[privotIndex]
    a[pivotIndex],a[right]=swap(a[pivotIndex],a[right])
    storeIndex=left
    for i in range(left, right-1):
        if (a[i] < pivotValue):
            a[storeIndex],a[i]=swap(a[storeIndex],a[i])
            storeIndex = storeIndex+1
    a[right], a[storeIndex]=swap(a[right], a[storeIndex])
    return storeIndex

def quicksort(a, left, right):
    if(right > left):
        pivotIndex=random.randint(left, right)
        pivotNewIndex=partition(a, left, right, pivotIndex)
        quicksort(a, left, pivotNewIndex-1)
        quicksort(a, privotNewIndex+1, right)
