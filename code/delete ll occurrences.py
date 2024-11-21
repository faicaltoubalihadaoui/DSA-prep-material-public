def deleteAllOccurances(self, head, x):
    if not head:
        return None

    # Step 1: Handle leading nodes with value `x`
    while head and head.data == x:
        head = head.next

    # Step 2: Traverse the list and remove occurrences of `x`
    current = head

    while current and current.next:
        if current.next.data == x:
            # Skip the node with value `x`
            current.next = current.next.next
        else:
            # Move to the next node
            current = current.next

    return head
            

def deleteAllOccurances(self, head, x):
    if not head:
        return None

    # Step 1: Skip all leading nodes with value `x`
    while head and head.data == x:
        head = head.next

    # Step 2: Traverse the rest of the list
    current = head
    prev = None

    while current:
        if current.data == x:
            # Skip the current node because we don't prev = prev.next
            if prev:
                prev.next = current.next
            current = current.next
        else:
            # Move both pointers forward
            prev = current
            current = current.next

    return head