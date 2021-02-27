def BuscaSentinela(vetor, chave):
	vetor.append(chave) # Coloca a chave na ultima posicao do vetor
	indice = 0 # Comeca testando da posicao 0 do vetor

	while vetor[indice] != chave: # Enquanto nao for a chave encontrada continua o laco
		indice += 1
	vetor.pop() # Retira o valor sentinela da ultima posicao

	if indice == len(vetor): # Se o indice esta igual o tamanho do vetor menos 1 significa que nao encontrou
		return -1 # Retorna -1

	return indice # Caso contrario, encontrou, retorna a posicao da chave no vetor


vetor = [1, 4, 5, 2, 42, 34, 54, 98, 89, 78, 67]
print (BuscaSentinela(vetor, 100))