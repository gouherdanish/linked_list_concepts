from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from node import Node

@dataclass
class LinkedList(ABC):
    head = None
    tail = None
    length = 0
    
    @abstractmethod
    def append(self, node):
        pass

    @abstractmethod
    def prepend(self, node):
        pass

    @abstractmethod
    def insert(self, node, index):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def pop_first(self):
        pass
    
    @abstractmethod
    def pop(self):
       pass

    @abstractmethod
    def remove(self, index):
        pass

    @abstractmethod
    def reverse(self):
        pass
