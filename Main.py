x = int(input())
arr = input().split(" ")
arr = [int(x) for x in arr]
arr.sort()
x = int(input())


def binarysearch(param):
    low = 0
    high = len(arr)-1
    while(low<=high):
        mid = int((low+high)/2)
        if arr[mid]<param:
            low = mid+1
        elif arr[mid]>param:
            high=mid-1
        else:
            return mid+1
    return -1




for i in range(x):
    print(binarysearch(int(input())))