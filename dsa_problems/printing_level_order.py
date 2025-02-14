from collections import deque


def print_level_order(node):
    queue = deque()
    queue.append(node)

    while queue:
        for _ in range(len(queue)):
            element = queue.popleft()
            print(element.val, end=",")
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)

        print()


print_level_order(root)
