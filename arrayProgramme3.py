# Array Programme Collection
'''
    1) Find Max|Largest Element
    2) Find Min|Smallest Element
    3) Find Second Largest Element
    4) Find Second Smallest Element
    5) Quick Sort
6) Merge Sort
    7) Find Duplicate|Repeat Element
8) First repeting Element
    9) Non Repeting Element
10) Re Arrange Array Alternating Positive & Negative
11) Remove Given Element
    12) Reverse An Array
    13) Reverse (Reccursive)
'''

#LargestElement
def largestElement(arr,size):

    maxElement = arr[0]

    for i in range(size):
        if arr[i] > maxElement:
            maxElement = arr[i]

    print("Largest Element In Array List : {}".format(maxElement))

#SmallestElement
def smallestElement(arr,size):

    minElement = arr[0]

    for i in range(size):
        if arr[i] < minElement:
            minElement = arr[i]

    print("Smallest Element In Array List : {}".format(minElement))

#SecondLargest / 2nd Largest Elemet
def secondLargestElement(arr,size):

    if size < 2:
        print("Array-List size should be GT 2")
        return
    
    larger = -99999
    secLarger = -99999

    for i in range(size):
        if arr[i] > larger:
            secLarger = larger
            larger = arr[i]

        elif arr[i] > secLarger and arr[i] != larger:
            secLarger = arr[i]

    if secLarger == -99999:
        print("Second Largest Element Not Found!")
    else:
        print("Second Largest Element : {}".format(secLarger))

#SecondSmallest / 2nd Smallest Element
def secondSmallestElement(arr,size):

    if size < 2:
        print ("Array-List size should be GT 2")
        return

    smaller = 99999
    secSmaller = 99999

    for i in range(size):
        if arr[i] < smaller:
            secSmaller = smaller
            smaller = arr[i]

        elif arr[i] < secSmaller and arr[i] != smaller:
            secSmaller = arr[i]

    if secSmaller == 99999:
        print("Second Smallest Element Not Foind")
    else:
        print("Second Smallest Element : {}".format(secSmaller))
        
#Duplicate-Repeat Element
def duplicateElement(arr,size):

    repeated = []
    
    for i in range(0,size):
        for j in range(i+1,size):
            if arr[i]==arr[j] and arr[i] not in repeated:
                repeated.append(arr[i])
    print("Duplicate | Repeated Element :{}".format(repeated))

# Reverse An Array-List
def reverseArrayList(arr,start,end):

    while start < end :
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

    print("Reverse Array-List : {}".format(arr))

def reverseArrayListReccursive(arr,start,end):

    if start >= end:
        return

        arr[start],arr[end] = arr[end],arr[start]
        reverseArrayListReccursive(arr,start+1,end-1)

    print("Reverse Array-List (Reccursive) : {}".format(arr))

# Non-Repeating Element
def nonRepeatingElement(arr,size):

    #insert All Array Elment in HASH TABLE
    mp = {}

    for i in range(size):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        mp[arr[i]] += 1

    print("Non Repeated Element :")
    for j in mp:
        if mp[j]==1:
            print(j,end=" ")

# Quick Sort(Recurssive)
def quickSortFunction(arr,size):
    quickSort(arr, 0, size-1)

def quickSort(arr,first,last):
    if first < last:

        splitPoint = partition(arr, first, last)

        quickSort(arr, first, splitPoint-1)#Last -1
        quickSort(arr, splitPoint+1, last)#First +1

def partition(arr,first,last):

    pivot = arr[first] 
    left = first
    right = last

    complete = False

    while not complete:
        while left <= right and arr[left] <= pivot:
            left = left + 1
            
        while right >= left and arr[right] >= pivot:
            right = right - 1


        if right < left :
            complete = True
        else:
            arr[left],arr[right] = arr[right],arr[left]

    arr[first],arr[right] = arr[right],arr[first]

    return right

#Main Function & Function Calling 
arr = [25,11,95,15,12,96,15,8,96,1,2,3,4,5,6]
print("Array - List : {}".format(arr))

size = len(arr)

largestElement(arr,size)
smallestElement(arr,size)
secondLargestElement(arr,size)
secondSmallestElement(arr,size)
duplicateElement(arr,size)
reverseArrayList(arr,0,size-1)
reverseArrayListReccursive(arr,0,size-1)
nonRepeatingElement(arr,size)
quickSortFunction(arr,size)
print("\nQuick Sort : {}".format(arr))
