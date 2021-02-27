def Heap(v,ini,t): #Função Heap que ordena em forma de arvore colocando o maior valor na raiz. 
    for i in range(ini,t): #Repetição que percorerar todo o vetor.
        cab = int((i+1)/2) #cab eh a variavel que indicara qual será o raiz do elemento.
        cab = cab -1
        if v[i]<v[cab]: #condição que verifica se o elemento é menor que a cabeça. #se menor trocara o elemento.
            aux = v[i]
            v[i]=v[cab]
            v[cab]=aux
            if cab>0: #quando trocado ele irá verificar se a cabeca da cabeca será menor. Assim retornando a função heap.
                Heap(v,cab,t)
    return v
def Sort(v): #função que ordenará o heap
    t = len(v)
    while t>1: #condição percore todo o vertor para trocar.
        Heap(v,1,t) #inicia com o heap
        aux = v[0] #sempre irá troca o primeiro elemento com o ultimo elemento o ultimo
        v[0] = v[t-1]
        v[t-1]=aux
        t=t-1 #sempre que é feita a troca um elemento, o ultimo elemento não será mais alterado.
    return v
v = [] #criação do vetor
print ("Digite os valores: ")
for i in range(10): #repetição para adição de numero ao vetor
    n = int(input()) #pega numero do usuario 
    v.append(n) #coloca numero no vetor.
print("Heap")
print(Heap(v,1,len(v))) #mostra Heap
print("Ordenação - HeapSort")
print(Sort(v)) #mostra vetor ordenado.