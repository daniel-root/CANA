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
    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node
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
    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.nref
    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None
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
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return 

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")
    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p
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
lista = DoublyLinkedList()
n = 1
while(n!=0):
    print("Escolha umas das opções:")
    print("0 - Sair")
    print("1 - Inserir na lista vazia")
    print("2 - Inserir no Inicio")
    print("3 - Inserir no Final")
    print("4 - Inserir depois de x")
    print("5 - Inserir antes de x")
    print("6 - Mostra lista")
    print("7 - Deleta do inicio")
    print("8 - Deleta do final")
    print("9 - Deleta valor x")
    print("10 - Reverter")
    print("11 - Encontra valor x - Busca Binária")
    print("12 - Encontra valor x - Busca Linear")
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
        lista.insert_at_start(a)
    elif (n==3):
        print("Digite um numero: ")
        a = int(input())
        lista.insert_at_end(a)
    elif (n==4):
        print("Digite um numero: ")
        a = int(input())
        print("Digite o número da lista")
        b = int(input())
        lista.insert_after_item(b, a)
    elif (n==5):
        print("Digite um numero: ")
        a = int(input())
        print("Digite o número da lista")
        b = int(input())
        lista.insert_before_item(b, a)
    elif (n==6):
        lista.traverse_list()
    elif (n==7):
        lista.delete_at_start()
    elif (n==8):
        lista.delete_at_end()
    elif (n==9):
        print("Digite um numero: ")
        x = int(input())
        lista.delete_element_by_value(x)
    elif (n==10):
        lista.reverse_linked_list()
    elif (n==11):
        print("Digite um numero: ")
        x = int(input())
        lista.sort_list(x)
    elif (n==12):
        print("Digite um numero: ")
        x = int(input())
        lista.sort_list1(x)
    else:
        print("Não encontrei")
    