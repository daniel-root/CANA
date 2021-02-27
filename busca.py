from random import randint
def busca(A,item):
  """Implementa pesquisa binária iterativamente."""
  esquerda, direita = 0, len(A) - 1
  while esquerda <= direita:
      meio = (esquerda + direita) // 2
      if A[meio] == item:
          print("Achei! ",meio+1,"ª posição.")
          return 0
      elif A[meio] > item:
          direita = meio - 1
      else: # A[meio] < item
          esquerda = meio + 1
  print("Elemento não está presente")
def binaria(A,item):
  l = 0
  r = len(A)-1
  while (l <= r):
    m = randint(l,r)
    if(A[m]==item):
      print("Achei! ",m+1,"ª posição.")
      return 0
    elif(A[m]<item):
      l = m + 1
    else:
      r = m - 1
  print("Elemento não está presente")
def linear(A,item):
  for i in range(len(A)):
    if (A[i]==item):
      print("Achei! ",i+1,"ª posição.")
      return 0
  print("Elemento não está presente")
def linearS(vetor,chave):
  vetor.append(chave) # Coloca a chave na ultima posicao do vetor
  i = 0 # Comeca testando da posicao 0 do vetor
  while vetor[i] != chave: # Enquanto nao for a chave encontrada continua o laco
    i+=1
  vetor.pop() # Retira o valor sentinela da ultima posicao
  if i == len(vetor): # Se o indice esta igual o tamanho do vetor menos 1 significa que nao encontrou
    print("Elemento não está presente") # Retorna -1
    return 0
  else:
    print("Achei! ",i+1,"ª posição.") # Caso contrario, encontrou, retorna a posicao da chave no vetor