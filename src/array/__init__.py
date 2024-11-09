def swapIfGreater(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]


def merge(arr1, arr2, n, m):
    # len of the imaginary single array:
    le = n + m

    # Initial gap:
    gap = (le // 2) + (le % 2)

    while gap > 0:
        # Place 2 pointers:
        left = 0
        right = left + gap
        while right < le:
            # case 1: left in arr1[]
            # and right in arr2[]:
            if left < n and right >= n:
                swapIfGreater(arr1, arr2, left, right - n)
            # case 2: both pointers in arr2[]:
            elif left >= n:
                swapIfGreater(arr2, arr2, left - n, right - n)
            # case 3: both pointers in arr1[]:
            else:
                swapIfGreater(arr1, arr1, left, right)
            left += 1
            right += 1
        # break if iteration gap=1 is completed:
        if gap == 1:
            break
        # Otherwise, calculate new gap:
        gap = (gap // 2) + (gap % 2)


if __name__ == "__main__":
    a=[12,12,12,12,12,12,12,12,12,12]
    b=[1,1,1,1,1,1,1,1,1,1]
    a=a+b
    print(a)