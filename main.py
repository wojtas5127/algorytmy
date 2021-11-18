from typing import Any

#Zadanie 1

class Node:
    value: Any
    next: 'Node'

    def __init__(self,value: Any, next: 'Node'):
        self.value = value
        self.next = next


class LinkedList:
    head: Node
    tail: Node

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __len__(self):
        z = self.head
        w = 0
        while z is not None:
            w += 1
            z = z.next
        return w

    def __str__(self):
        w=""
        z = self.head
        while z is not None:
            if z.next is None:
                w += str(z.value)
            else:
                w += str(z.value) + ' -> '
            z = z.next
        return w

    def push(self, value: Any) -> None:
        if self.head == None:
            self.head = Node(value,None)
            self.tail = self.head
        else:
            z = self.head
            self.head = Node(value,z)

    def append(self, value: Any) -> None:
        if self.tail == None:
            self.tail = Node(value,None)
            self.head = self.tail
        else:
            z = self.head
            while z is not None:
                if z.next is None:
                    z.next = Node(value,None)
                    self.tail = z.next
                    z = None
                else:
                    z = z.next

    def node(self, at: int) -> Node:
        z = self.head
        x = 0
        while z is not None:
            if x == at:
                return z
            x += 1
            z = z.next

    def insert(self, value: Any, after: Node) -> None:
        z = self.head
        while z is not None:
            if z == after:
                y = z.next
                z.next = Node(value,y)
                z = None
            else:
                z = z.next

    def pop(self) -> Any:
        z = self.head
        self.head = z.next
        return z.value

  

    def remove(self, after: Node) -> Any:
        z = self.head
        while z is not None:
            if z == after:
                z.next = z.next.next
                z = None
            else:
                z = z.next




# lista = LinkedList()
#
# lista.push(1)
# lista.push(0)
# assert str(lista) == '0 -> 1'
#
#
# lista.append(9)
# lista.append(10)
# assert str(lista) == '0 -> 1 -> 9 -> 10'
#
#
# middle_node = lista.node(at=1)
# lista.insert(5, after=middle_node)
# assert str(lista) == '0 -> 1 -> 5 -> 9 -> 10'
#
#
# first_element = lista.node(at=0)
# returned_first_element = lista.pop()
# assert first_element.value == returned_first_element
#
#
# second_node = lista.node(at=1)
# lista.remove(second_node)
# assert str(lista) == '1 -> 5'
#
# print(len(lista))
# #
# print(lista)



#Zadanie 2

class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()


    def push(self, element: Any) -> None:
        self._storage.append(element)

    

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        w = ""
        z = self._storage.head
        while z is not None:
            if z.next is None:
                w += str(z.value)
            else:
                w += str(z.value) + '\n'
            z = z.next
        return w





# stack = Stack()
#
# assert len(stack) == 0
#
#
# stack.push(3)
# stack.push(10)
# stack.push(1)
# assert len(stack) == 3
#
#
# top_value = stack.pop()
# assert top_value == 1
#
#
# assert len(stack) == 2
#
# print(stack)


#Zadanie 3


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)
    def __str__(self):
        w = ""
        z = self._storage.head
        while z is not None:
            if z.next is None:
                 w += str(z.value)
            else:
                w += str(z.value) +", "
            z = z.next
        return w



    def peek(self) -> Any:
        return self._storage.node(at=0)

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()




# queue = Queue()
#
#
#
# assert len(queue) == 0
#
# queue.enqueue('klient1')
# queue.enqueue('klient2')
# queue.enqueue('klient3')
# assert str(queue) == 'klient1, klient2, klient3'
#
#
# client_first = queue.dequeue()
# assert client_first == 'klient1'
# assert str(queue) == 'klient2, klient3'
# assert len(queue) == 2
#
# print(queue)

