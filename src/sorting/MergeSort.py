def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
    return arr

# mergesort without passing extra space
def mergeinplace(arr,s,e):
    if e-s<=1:
        return arr
    mid=s+ (e-s)//2
    mergeinplace(arr,s,mid)
    mergeinplace(arr,mid+1,e)


    i=s
    j=mid
    k=0
    mix=[0]*(e-s)
    print(e-s)
    print(mix)

    while i<mid and j<e:
        if arr[i]<arr[j]:
            mix[k]=arr[i]
            i+=1
        else:
            mix[k]=arr[j]
            j+=1
        k+=1
    while i<mid:
        mix[k]=arr[i]
        i+=1
        k+=1
    while j<e:
        mix[k]=arr[j]
        j+=1
        k+=1
    for i in range(len(mix)):
        arr[s+i]=mix[i]



    return arr

# Time complexity for mergesort is O(nlogn)




if __name__=="__main__":
    print("Hello World")
    arr=[12,11,13,5,6,7]
    print(mergeSort(arr))
    print(mergeinplace(arr,0,len(arr)-1))
