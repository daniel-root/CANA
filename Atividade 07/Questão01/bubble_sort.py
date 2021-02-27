def bubbleSort(v):
	arr = v
	for j in range(1,len(arr)):
		for i in range(0,len(arr)-1):
			if(arr[i]>arr[i+1]):
				aux = arr[i+1]
				arr[i+1]=arr[i]
				arr[i] = aux
	return arr