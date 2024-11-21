from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque() # actual stack
        self.q2 = deque() # tmp 

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        if not self.empty():
            return self.q1.popleft()
        

    def top(self) -> int:
        if not self.empty():
            return self.q1[0]

    def empty(self) -> bool:
        return self.q1 == deque()