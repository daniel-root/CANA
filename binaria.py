def binaria(A, esquerda, direita, item):
  if direita < esquerda:
    print("Elemento não está presente")
    return 0
  meio = (esquerda + direita) // 2
  if A[meio] == item:
    print("Achei! ",meio+1,"ª posição.")
  elif A[meio] > item:
    return binaria(A, esquerda, meio - 1, item)
  else:
    return binaria(A, meio + 1, direita, item)
A = [2,40,35,7,5,20,32,46,12,87,34,23,67]
print(sorted(A))
binaria(sorted(A), 0, len(A) - 1, 46)