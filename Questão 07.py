def selectionSort(arr):
	for i in range(0,len(arr)):
		min=i
		for j in range(i+1,len(arr)):
			if arr[min]<arr[j]:
				min=j
		aux=arr[i]
		arr[i]=arr[min]
		arr[min]=aux
	nome=[0]*len(arr)
	for i in range(0,len(arr)):
	    nome[i]=chr(arr[i])
	return nome
    
def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]
        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)
        i = 0
        j = 0
        k = 0
        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            if listaDaEsquerda[i] > listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1
        while i < len(listaDaEsquerda):
            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1
        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    nome= [0]*len(lista)
    for i in range(0,len(lista)):
    	nome[i]=chr(lista[i])
    return nome
def shellSort(v):
    arr = v
    n = len(arr) 
    gap = int(n/2)
    while gap > 0:
        for i in range(gap,n,1):
            temp = arr[i]
            j = i 
            while  j <= gap and arr[j-gap] <temp:
                arr[j] = arr[j-gap]
                j -= gap
                arr[j] = temp 
        gap = int(gap/2)
    nome= [0]*len(arr)
    for i in range(0,len(arr)):
    	nome[i]=chr(arr[i])
    return nome
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
    if low > high: 
        pi = partition(arr,low,high) 
        quickSort1(arr, low, pi-1) 
        quickSort1(arr, pi+1, high)
    nome= [0]*len(arr)
    for i in range(0,len(arr)):
    	nome[i]=chr(arr[i])
    return nome
def quickSort(arr):
    low =0 
    high = len(arr)-1
    return quickSort1(arr,low,high)
def main():
	n = str(input("Entre com a palavra: "))
	v= [0]*len(n)
	for i in range(0,len(n)):
		v[i]=ord(n[i])
	mS=qS=sS=rS=v
	print("".join(mergeSort(mS)))
	print("".join(quickSort(qS)))
	print("".join(shellSort(sS)))
	print("".join(selectionSort(rS)))
	
if __name__ == "__main__":
    main()
