def partition(v,low,high):
    arr = v
    i = ( low-1 )
    pivot = arr[high]
  
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort1(arr,low,high):
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort1(arr, low, pi-1) 
        quickSort1(arr, pi+1, high)
    return arr
def quickSort(arr):
    low =0 
    high = len(arr)-1
    return quickSort1(arr,low,high)