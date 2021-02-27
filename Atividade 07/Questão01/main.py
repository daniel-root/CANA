import random
import math
import timeit
import matplotlib.pyplot as plt
from selection_sort import selectionSort
from insertion_sort import insertionSort
from bubble_sort import bubbleSort
from quick_sort import quickSort
from shell_sort import shellSort
from radix_sort import radixSort
from counting_sort import countingSort
from bucket_sort import bucketSort
from merge_sort import mergeSort
from heap_sort import heapSort

timeSelection = []
timeInsertion = []
timeBubble = []
timeQuick = []
timeShell = []
timeRadix = []
timeCounting = []
timeBucket = []
timeMerge = []
timeHeap = []

tamanhos = [1000, 3000, 6000, 9000, 12000, 18000, 21000, 24000]
def randArray(length):
	array = []
	tmp = 0
	while tmp < length:
		num = random.randint(1, length*10)
		if num not in array:
			array.append(num)
			tmp += 1
	return array

def timePopulate():
	for numTamanhos in tamanhos:
		base = []
		base = randArray(numTamanhos)

		_tmp = list(base)
		timeSelection.append(timeit.timeit("selectionSort({})".format(_tmp), \
		setup="from __main__ import selectionSort", \
		number=1))

		_tmp = list(base)
		timeInsertion.append(timeit.timeit("insertionSort({})".format(_tmp), \
		setup="from __main__ import insertionSort", \
		number=1))

		_tmp = list(base)
		timeBubble.append(timeit.timeit("bubbleSort({})".format(_tmp), \
		setup="from __main__ import bubbleSort", \
		number=1))

		_tmp = list(base)
		timeQuick.append(timeit.timeit("quickSort({})".format(_tmp), \
		setup="from __main__ import quickSort", \
		number=1))

		_tmp = list(base)
		timeShell.append(timeit.timeit("shellSort({})".format(_tmp), \
        setup="from __main__ import shellSort", \
        number=1))
		
		_tmp = list(base)
		timeRadix.append(timeit.timeit("radixSort({})".format(_tmp), \
		setup="from __main__ import radixSort", \
        number=1))

		_tmp = list(base)
		timeCounting.append(timeit.timeit("countingSort({})".format(_tmp), \
        setup="from __main__ import countingSort", \
        number=1))

		_tmp = list(base)
		timeBucket.append(timeit.timeit("bucketSort({})".format(_tmp), \
        setup="from __main__ import bucketSort", \
        number=1))

		_tmp = list(base)
		timeMerge.append(timeit.timeit("mergeSort({})".format(_tmp), \
		setup="from __main__ import mergeSort", \
		number=1))

		_tmp = list(base)
		timeHeap.append(timeit.timeit("heapSort({})".format(_tmp), \
		setup="from __main__ import heapSort", \
		number=1))

		print("Lista de Tamanho {}".format(numTamanhos),"ordenada")

def axis():
	timePopulate()

	plt.plot(tamanhos, timeSelection, label="Selection Sort")
	plt.plot(tamanhos, timeInsertion, label="Insertion Sort")
	plt.plot(tamanhos, timeBubble, label="Bubble Sort")
	plt.plot(tamanhos, timeQuick, label="QuickSort")
	plt.plot(tamanhos, timeShell, label="ShellSort")
	plt.plot(tamanhos, timeRadix, label="RadixSort")
	plt.plot(tamanhos, timeCounting, label="CountingSort")
	plt.plot(tamanhos, timeBucket, label="BucketSort")
	plt.plot(tamanhos, timeMerge, label="MergeSort")
	plt.plot(tamanhos, timeHeap, label="HeapSort")

def graphic():
	plt.legend(loc='upper center', shadow=True).get_frame().set_facecolor('0.90')
	plt.xlabel('Tamanho(int)')
	plt.ylabel('Tempo(s)')
	plt.show()

def main():
	axis()
	graphic()

if __name__ == "__main__":
	main()
