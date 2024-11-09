def arraysorted_or_not(arr, n):
    if n==1:
        return True
    return arr[n-1]>=arr[n-2] and arraysorted_or_not(arr, n-1)

def linearsearch(arr, n, key):
    if n==0:
        return -1
    if arr[n-1]==key:
        return n-1
    return linearsearch(arr, n-1, key)

def linearsearchindexes(arr,n,key,list):
    if n==0:
        return list
    if arr[n-1]==key:
        list.append(n-1)
    return linearsearchindexes(arr,n-1,key,list)

def linearsearchindexes_withoutlist_argument(arr,i,key):
    if i==len(arr):
        return []
    if arr[i]==key:
        return [i]+linearsearchindexes_withoutlist_argument(arr,i+1,key)
    return linearsearchindexes_withoutlist_argument(arr,i+1,key)


def find(arr,target,n):
    if n==0:
        return False
    if arr[n-1]==target:
        return True
    return find(arr,target,n-1)

def rotate_binarysearch(arr,s,e,target):
    if s>e:
        return -1
    mid=(s+(e-s)//2)
    if arr[mid]==target:
        return mid
    if arr[s]<=arr[mid]:
        if target>=arr[s] and target<=arr[mid]:
            return rotate_binarysearch(arr,s,mid-1,target)
        else:
            return rotate_binarysearch(arr,mid+1,e,target)
    if target>=arr[mid] and target<=arr[e]:
        return rotate_binarysearch(arr,mid+1,e,target)

if __name__=="__main__":
    print(rotate_binarysearch([4,5,6,7,0,1,2],0,6,0))