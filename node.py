from dataclasses import dataclass, field

@dataclass
class Node:
    value: int
    next = None
    prev = None
