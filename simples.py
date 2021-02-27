from counting_sort import countingSort
from busca import busca
from busca import linear
class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")
    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n
    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None
    def sort_list(self,x):
        v = []
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                v.append(n.item)
                n = n.nref
        v = countingSort(v)
        busca(v,x)
    def sort_list1(self,x):
        v = []
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                v.append(n.item)
                n = n.nref
        v = countingSort(v)
        linear(v,x)
    def traverse_list(self):
        v = []
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                v.append(n.item)
                n = n.nref
        print(v)
lista = DoublyLinkedList()
n = 1
while(n!=0):
    print("Escolha umas das opções:")
    print("0 - Sair")
    print("1 - Inserir na lista vazia")
    print("2 - Inserir")
    print("3 - Deletar")
    print("4 - Encontra valor x - Busca Binária")
    print("5 - Encontra valor x - Busca Linear")
    print("6 - Mostra Lista")
    n=int(input())

    if (n==0):
        break;
    elif (n==1):
        print("Digite um numero: ")
        a = int(input())
        lista.insert_in_emptylist(a)
    elif (n==2):
        print("Digite um numero: ")
        a = int(input())
        lista.insert_at_end(a)
    elif (n==3):
        lista.delete_at_end()
    elif (n==4):
        print("Digite um numero: ")
        x = int(input())
        lista.sort_list(x)
    elif (n==5):
        print("Digite um numero: ")
        x = int(input())
        lista.sort_list1(x)
    elif(n==6):
        lista.traverse_list()
    else:
        print("Não encontrei")