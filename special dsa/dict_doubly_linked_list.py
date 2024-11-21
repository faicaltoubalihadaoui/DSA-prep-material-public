""" 
Operation	        Time Complexity
Insert	            O(1)
Remove	            O(1)
Lookup (Find)	    O(1)
Get Ordered List	O(n) 

"""

"""
dict : provides O(1) lookup for quick access to elements
double linked list : maintains the order of elements and allows O(1) insertion and deletion
example : LRU cache
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DictLinkedList:
    def __init__(self):
        self.dict = {}
        self.head = None
        self.tail = None

    def insert(self, value):
        if not value in self.dict:
            # add the value

            new_node = ListNode(value)
            self.dict[value] = new_node

            if not self.head:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            return True
        return False

    def remove(self, value):
        if value in self.dict:
            node = self.dict[value]

            if node.prev:
                node.prev.next = node.next
            else:  # Node was the head
                self.head = node.next

            if node.next:
                node.next.prev = node.prev
            else:  # Node was the tail
                self.tail = node.prev

            del self.dict[value]
            return True
        return False

    def find(self, value):
        return value in self.dict

    def get_ordered_values(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values
