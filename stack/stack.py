# Part 1

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   
"""

"""
Instructions from readme:

Should have the methods: push, pop, and len.

    push adds an item to the top of the stack.
    pop removes and returns the element at the top of the stack
    len returns the number of elements in the stack.

"""

# 1
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if not self.__len__():
#             return None
#         return self.storage.pop()

# 2

class Stack:
    def __init__(self):
        self.storage = LinkedList()
    
    def __len__(self):
        return len(self.storage)
    
    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.remove_from_tail()

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def add_to_tail(self, value):
        new_node = Node(value, None)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def remove_from_tail(self):
        if self.length > 0:
            current = self.head
            previous = None
            while current.next != None:
                previous = current
                current = current.get_next()
            if previous != None:
                previous.set_next(None)
                self.tail = previous
                self.length -= 1
                return current.value
            else:
                self.head = None
                self.tail = None
                self.length = 0
                return current.value
        else:
            return None