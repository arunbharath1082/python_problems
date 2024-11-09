def QuickSort(arr,low,high):
    if low >high:
        return
    s=low
    e=high
    p=s+(e-s)//2
    pivot=arr[p]

    while s<=e:
        while arr[s]<pivot:
            s+=1
        while arr[e]>pivot:
            e-=1

        if s<=e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1
    QuickSort(arr,low,e)
    QuickSort(arr,s,high)


if __name__=="__main__":
    arr=[12,11,13,5,6,7]
    QuickSort(arr,0,len(arr)-1)
    print(arr)