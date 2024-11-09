def PascalTriangle():
    def nCr(n,r):
        res=1
        for i in range(r):
            res*=(n-i)
            res//=(i+1)
        return res
    # For particular row of pascal triangle
    row=4
    print("Pascal Triangle for row ",row)
    for i in range(1,row+1):
        print(nCr(row-1,i-1),end=" ")

    # For particular row and column of pascal triangle
    row=4
    col=2
    print("\nPascal Triangle for row ",row," and column ",col)
    print(nCr(row-1,col-1))

    # For whole pascal triangle
    row=4
    print("\nPascal Triangle for n ",row)
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(nCr(i-1,j-1),end=" ")
        print()

# It is used for finding the maximum sum of subarray
def kadanes_Algorithm(arr):

    maxi=arr[0]
    add=0
    for i in range(len(arr)):
        add+=arr[i]
        if add>maxi:
            maxi=add
        if add<0:
            add=0
    return maxi

def Next_permutation_in_lexicographic_order(arr):
    n=len(arr)
    breakIndex=-1
    # find the break index, which is ith element is smaller than i+1th element
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            breakIndex=i
            break
    # if no break index found, then it is last permutation
    if breakIndex==-1:
        return arr[::-1]
    # find the element which is greater than break index element and swap it
    for i in range(n-1,breakIndex,-1):
        if arr[i]>arr[breakIndex]:
            arr[i],arr[breakIndex]=arr[breakIndex],arr[i]
            break
    # reverse the element from break index+1 to end
    arr[breakIndex+1:]=arr[breakIndex+1:][::-1]
    return arr





if __name__ == '__main__':
    print(Next_permutation_in_lexicographic_order([2, 1, 5, 4, 3, 0, 0]))