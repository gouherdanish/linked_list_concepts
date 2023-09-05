from linked_list import LinkedList
from node import Node

from dataclasses import dataclass, field

@dataclass
class DLL(LinkedList):
    head: Node
    tail: Node
    length: int = field(default=0,repr=False)
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __str__(self) -> str:
        nodes = '<->'.join([str(node.value) for node in self]) if self.head else ''
        return f'DLL({nodes})'
    
    def get(self, index):
        if index < -1 or index > self.length:
            raise Exception("Usage: Invalid Index")
        if index == -1:
            return self.tail
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, node):
        if index < -1 or index > self.length:
            raise Exception("Usage: Invalid Index")
        if index == -1:
            index = self.length - 1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = node.value
    
    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1

    def prepend(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.tail.prev = node
            self.head = node
        self.length += 1

    def insert(self, node, index):
        if index < -1 or index > self.length:
            raise Exception('Invalid Index')
        elif index == 0:
            self.prepend(node)
        elif index == -1:
            self.append(node)
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            node.next = temp.next
            node.prev = temp
            temp.next.prev = node
            temp.next = node
            self.length += 1

    def create(self,*args):
        if len(args):
            for val in args:
                self.append(Node(val))

    def pop_first(self):
        if self.length == 0:
            return None
        node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        node.next = None
        node.prev = None
        self.length -= 1
        return node
    
    def pop(self):
        if self.length == 0:
            return None
        node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        node.next = None
        node.prev = None
        self.length -= 1
        return node

    def remove(self, index):
        if index < -1 or index > self.length or self.length == 0:
            raise Exception('Invalid Index')
        if index == 0:
            return self.pop_first()
        elif index == -1 or index == self.length - 1:
            return self.pop()
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            temp = curr.next
            curr.next = curr.next.next
            curr.next.next.prev = curr
            temp.next = None
            temp.prev = None
            self.length -= 1
            return temp

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            print(prev, curr, next)
            prev = curr
            curr = next
        self.head, self.tail = self.tail, self.head
        return self