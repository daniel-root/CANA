def insertionSort(v):
	arr = v
	for i in range(0,len(arr)):
		x = arr[i]
		j = i-1
		while j>=0 and arr[j] >x:
			arr[j+1]=arr[j]
			j=j-1
			arr[j+1]=x
	return arr