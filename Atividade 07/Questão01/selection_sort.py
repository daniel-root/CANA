def selectionSort(v):
	arr = v
	for i in range(0,len(arr)):
		min=i
		for j in range(i+1,len(arr)):
			if arr[min]>arr[j]:
				min=j
		aux=arr[i]
		arr[i]=arr[min]
		arr[min]=aux
	return arr