
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Pila: 
    def __init__(self):
        self.top = None

    def push(self, x):
        new = Node(x)
        new.next = self.top
        self.top = nuevo

    def pop(self):
        if self.top is None: 
            return None
        aux = self.top.data
        self.top = self.top.next
        return aux

    def esta_vacia(self): 
        return self.top is None


class Cola: 
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        nuevo = Node(item)
        if self.head is None:
            self.head = nuevo
            self.tail = nuevo
        else:
            self.tail.next = nuevo
            self.tail = nuevo

    def dequeue(self):
        if self.head is None: 
            return None
        aux = self.head.data
        self.head = self.head.next
        return aux
