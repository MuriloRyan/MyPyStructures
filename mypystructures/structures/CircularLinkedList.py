#Used for the list of notes
from typing import Any

class Node:
    def __init__(self, data: Any):
        self.data: Any | None = data
        self.next: Node | None = None

    def __str__(self):
        return str(self.data)

class CircularLinkedList:
    def __init__(self, node_class=Node):
        self.root = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if not self.root:
            self.root = new_node
            self.root.next = self.root

            self.tail = self.root
            self.tail.next = self.root.next
        
        else:
            self.tail.next = new_node 
            self.tail.next.next = self.root
            self.tail = self.tail.next
            

    def find_one(self, data):
        current_node = self.root
        index = 0

        while current_node.data != data:
            current_node = current_node.next
            index += 1

             #When the list starts to repeat itself, so the item dosent exist
            if current_node == self.root:
                raise StopIteration

        return {'item': current_node.data, 'index': index}
    
    
    
    def __getitem__(self, steps):
        current_node = self.root
        i = 0

        while i <= steps:
            node = current_node
            current_node = current_node.next

            i += 1

        return node
    
    def __iter__(self):
        self._iter_current_node = self.root
        self._iter_stop = False
        return self

    def __next__(self):
        if self._iter_current_node is None:
            raise StopIteration

        # if the next item is different of self.root
        # ex: A - B. A has B as next
        if self._iter_current_node.next != self.root:
            node = self._iter_current_node
            self._iter_current_node = self._iter_current_node.next

            return node
        
        elif self._iter_stop == True:
            raise StopIteration

        # if the current node has root as next node
        # ex: A - B. A has A as next so its the last node
        elif self._iter_current_node.next == self.root:
            node = self._iter_current_node
            self._iter_stop = True

            return node

    def __repr__(self):
        if self.root is None:
            return "Circular[]"
        object_list = []

        current_node = self.root
        while True:
            object_list.append(str(current_node))
            print(current_node)

            current_node = current_node.next
            if current_node == self.root:
                break

        return f'Circular{str(object_list)}'

