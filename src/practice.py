def funct(arr):
    length=len(arr)
    if length<=1:
        return arr
    mid=length//2
    L=arr[:mid]
    R=arr[mid:]
    funct(L)
    funct(R)
    i=j=k=0

    while(i<len(L) and j<len(R)):
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while(i<len(L)):
        arr[k]=L[i]
        i+=1
        k+=1
    while(j<len(L)):
        arr[k]=R[j]
        j+=1
        k+=1
    return arr

if __name__=="__main__":
    arr=[12,11,13,5,6,7]
    print(funct(arr))