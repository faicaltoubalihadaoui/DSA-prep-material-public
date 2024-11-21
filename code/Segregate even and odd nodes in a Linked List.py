class Solution:
    def divide(self, head):
        # code here
        if not head:
            return None

        even_head = None
        odd_head = None
        even_tail = even_head
        odd_tail = odd_head
        current = head
        while current:
            next_node = current.next
            ## Disconnecting the Node is extremely important to not assign the whole remaining of the linked list
            current.next = None
            if current.data% 2 == 0:
                if not even_head:
                    even_head = current
                    even_tail = even_head
                else:
                    even_tail.next = current
                    even_tail = even_tail.next
            else:
                if not odd_head:
                    odd_head = current
                    odd_tail = odd_head
                else:
                    odd_tail.next = current
                    odd_tail = odd_tail.next
            current = next_node
        if even_tail:
            even_tail.next = odd_head
        return even_head if even_head else odd_head
