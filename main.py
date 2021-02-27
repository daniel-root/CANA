import random
import math
import timeit
import matplotlib.pyplot as plt
from counting_sort import countingSort
from busca import busca
from busca import linear
from busca import binaria
from busca import linearS

timeLinear = []
timeBinaria = []
timeBinariaS = []
timeLinearS = []

tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

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
		n = random.randint(1, numTamanhos)
		#print(n)
		
		_tmp = list(countingSort(base))
		#print (_tmp)
		timeLinear.append(timeit.timeit("linear({},{})".format(_tmp,n), \
		setup="from __main__ import linear", \
		number=1))

		_tmp = list(countingSort(base))
		timeBinaria.append(timeit.timeit("busca({},{})".format(_tmp,n), \
		setup="from __main__ import busca", \
		number=1))

		_tmp = list(countingSort(base))
		#print (_tmp)
		timeBinariaS.append(timeit.timeit("binaria({},{})".format(_tmp,n), \
		setup="from __main__ import binaria", \
		number=1))

		_tmp = list(countingSort(base))
		#print (_tmp)
		timeLinearS.append(timeit.timeit("linearS({},{})".format(_tmp,n), \
		setup="from __main__ import linearS", \
		number=1))

		#print("Lista de Tamanho {}".format(numTamanhos),"ordenada")

def axis():
	timePopulate()

	plt.plot(tamanhos, timeLinear, label="Busca Linear")
	plt.plot(tamanhos, timeBinaria, label="Busca Binária")
	plt.plot(tamanhos, timeLinearS, label="Busca Linear Sentinela")
	plt.plot(tamanhos, timeBinariaS, label="Busca Binária Simples")

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
