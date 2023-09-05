from linked_list import LinkedList
from node import Node

from dataclasses import dataclass, field

@dataclass
class CSLL(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    def __str__(self) -> str:
        nodes = '->'.join([str(node.value) for node in self]) if self.head else ''
        return f'CSLL({nodes})'

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
            index = self.length -1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = node.value

    def prepend(self, node):
        if self.length == 0:
            node.next = node
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.next = self.head
            self.head = node
        self.length += 1

    def append(self, node):
        if self.length == 0:
            node.next = node
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node
        self.length += 1
            
    def insert(self, node, index):
        if index < -1 or index > self.length:
            raise Exception('Invalid Index')
        elif index == 0:
            self.prepend(node)
        elif index == -1:
            self.append(node)
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
            self.length += 1

    def create(self,*args):
        if len(args):
            for val in args:
                self.append(Node(val))

    def pop_first(self):
        if self.length == 0:
            raise Exception('Empty')
        temp = self.head
        if self.length == 1:
            self.head == None
            self.tail == None
            self.tail.next = None
            self.head.next = None
        else:
            self.tail.next = self.head.next
            self.head = self.tail.next
        temp.next = None
        self.length -= 1
        return temp

    def pop(self):
        if self.length == 0:
            raise Exception('Empty')
        temp = self.tail
        if self.length == 1:
            self.tail.next = None
            self.head.next = None
            self.head = None
            self.tail = None
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            curr.next = self.tail.next
            self.tail = curr
        temp.next = None
        self.length -= 1
        return temp
        
    def remove(self, index):
        if index < -1 or index > self.length or self.length == 0:
            raise Exception('Invalid Index')
        elif index == 0:
            return self.pop_first()
        elif index == -1:
            return self.pop()
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            temp = curr.next
            curr.next = curr.next.next
            temp.next = None
            self.length -= 1
            return temp
        
    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head, self.tail = self.tail, self.head
        return self
