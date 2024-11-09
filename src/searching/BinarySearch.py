def binarySearch(arr,target):

    start=0
    end=len(arr)-1
    while start<=end:
        mid = start + (end - start) // 2
        if arr[mid]<target:
            start=mid+1
        elif arr[mid]>target:
            end=mid-1
        else:
            return mid
    return -1


# when we do not know the order of the array we use this
def ordereAgnosticBinarysearch(arr,target):

    start=0
    end=len(arr)-1

    isAsce=arr[start]<arr[end]
    print(isAsce)
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==target:
            return mid
        if isAsce:
            if arr[mid]<target:
                start=mid+1
            else:
                end=mid-1
        else:
            if arr[mid]>target:
                start=mid+1
            else:
                end=mid-1
    return -1

def celing_BinarySearch(arr,target):
    if target>arr[len(arr)-1]:
        return -1
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==target:
            return mid
        if arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return start

def floor_BinarySearch(arr,target):
    if target<arr[0]:
        return -1
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==target:
            return mid
        if arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return end

# Amazon Question.. given infinite sorted array, find the target element
def Infinite_SortedArray(arr,target):
    start=0
    end=1
    while target>arr[end]:
        newStart=end+1
        end=end+(end-start+1)*2
        start=newStart
    return binarySearch(arr[start:end+1],target)

# array which has increasing order and then decreasing order
# find the peak or highest number

def Biotonic_Array(arr):
    s=0
    e=len(arr)-1
    ans=0
    while s<e:

        mid=s+(e-s)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            ans=mid
            break
        elif arr[mid]>arr[mid-1]:
            s=mid+1
        elif arr[mid]>arr[mid+1]:
            e=mid
    return ans

def findElement_in_BiotonicArray(arr,target):
    peak=Biotonic_Array(arr)
    if arr[peak]==target:
        return peak
    left= binarySearch(arr[:peak],target)
    right= ordereAgnosticBinarysearch(arr[peak:],target)
    if left==-1 and right==-1:
        return -1
    elif left!=-1:
        return left
    else:
        return right+peak

# find the pivot element in the rotated sorted array
# this will not work with duplicate values
def pivot_in_rotatedSortedArray(arr):
    s=0
    e=len(arr)-1

    while s<e:
        mid=s+(e-s)//2

        if mid<e and arr[mid]>arr[mid+1]:
            return mid
        elif mid>s and arr[mid]<arr[mid-1]:
            return mid-1
        elif arr[s]>=arr[mid]:
            e=mid-1
        else:
            s=mid+1
    return -1

def pivot_in_rotatedSortedArray_WithDuplicates(arr):
    s=0
    e=len(arr)-1

    while s<e:
        mid=s+(e-s)//2

        if mid<e and arr[mid]>arr[mid+1]:
            return mid
        elif mid>s and arr[mid]<arr[mid-1]:
            return mid-1
    #     if elements at middele, start, end are equal then we will skip the duplicates
        if arr[mid]==arr[s] and arr[mid]==arr[e]:
#             skip the duplicates
#            NOTE: what if these elements at start and end were the pivot element
            if arr[s]>arr[s+1]:
                return s
            s+=1
            # check whether end is pivot or not
            if arr[e]<arr[e-1]:
                return e-1
            e-=1
        # leftside is sorted, so the pivot is in rightside
        elif  arr[s]<arr[mid] or (arr[s]==arr[mid] and arr[mid]>arr[e]):
            s=mid+1
        else:
            e=mid-1
    return -1

def findElement_sortedRotatedArray(arr,target):
    pivot= pivot_in_rotatedSortedArray_WithDuplicates(arr)
    if pivot==-1:
        return binarySearch(arr,target)
    if arr[pivot]==target:
        return pivot
    print(arr[:pivot])
    left= binarySearch(arr[:pivot],target)
    print(left)
    print(arr[left])
    if left!=-1:
        return left
    print(arr[pivot+1:])
    right=binarySearch(arr[pivot+1:],target)
    print(right)
    if right!=-1:
        return right+pivot+1
    return -1

# search in 2D matrix
# matrix is sorted in row and column wise
# log(n)
#  matrix=[
#      [10,20,30,40],
#      [15,25,35,45],
#      [28,29,38,47],
#      [33,34,39,50]
#  ]

def BinarySearch_sorted2D_Matrix(matrix,target):
    if len(matrix)==0:
        return -1
    row=0
    col=len(matrix[0])-1

    while row<len(matrix) and col>=0:
        if matrix[row][col]==target:
            return list([row,col])

        if matrix[row][col]>target:
            col-=1
        else:
            row+=1
    return -1
if __name__=="__main__":
    arr=[15,18,2,6,12]
    matrix=[[10,20,30,40],[15,25,35,45],[28,29,38,47],[33,34,39,50]]
    print(BinarySearch_sorted2D_Matrix(matrix,38))

