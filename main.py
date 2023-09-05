from csll import CSLL
from sll import SLL
from dll import DLL
from node import Node

if __name__ == '__main__':
    l = SLL()
    l.create(1,2,4,0)
    print(l)
    print(l.max())
    # l.prepend(Node(10))
    # print(l,l.length)
    # l.prepend(Node(20))
    # print(l,l.length)
    # l.prepend(Node(30))
    # print(l,l.length)
    # l.insert(Node(15),0)
    # print(l,l.length)
    # print(l.head,l.head.next, l.tail, l.tail.next)
    # l.reverse()
    # print(l,l.length)
    # print(l.head,l.head.next, l.tail, l.tail.next)
    # l.remove(1)
    # print(l,l.length)
    # print(l.head,l.head.next, l.tail, l.tail.next)
    # l.pop()
    # print(l,l.length) 
    # print(l.head,l.head.next, l.tail, l.tail.next)
    # l.pop_first()
    # print(l,l.length)
    # print(l.head,l.head.next, l.tail, l.tail.next)

    # idx = 2
    # print(l.get(idx))
    # l.set(idx,Node(200))
    # print(l,l.length)