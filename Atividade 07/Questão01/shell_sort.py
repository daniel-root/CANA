def shellSort(v):
    arr = v
    n = len(arr) 
    gap = int(n/2)
    while gap > 0:
        for i in range(gap,n,1):
            temp = arr[i]
            j = i 
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
                arr[j] = temp 
        gap = int(gap/2)
    return arr