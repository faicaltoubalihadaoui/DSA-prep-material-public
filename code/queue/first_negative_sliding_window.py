# O (n)
from collections import deque
def first_negative_integer(arr, k):
    if not arr or  k <= 0 or k > len(arr):
        return []
    
    res = []
    q = deque()

    for i in range(len(arr)):
        if arr[i] < 0:
            q.append(i)

        # current window is  [ i - k + 1 , i + k -1]
        # if the element is always within the window we let it, if not we remove it 
        if q and not  (i + k -1 >= q[0] >= i - k + 1):
            q.popleft()    

        if i >= k - 1:
            if q:
                res.append(arr[q[0]])
            else:
                res.append(0)

    return res 

arr = [-8, 2, 3, -6, 10]
print(first_negative_integer(arr, 2))




#O (nk)
from collections import deque
class Solution:
    def FirstNegativeInteger(self, arr, k): 
        if not arr or k <= 1 or k > len(arr):
            return []
        
        i = 0
        res = []
        while i + k <= len(arr):
            q = deque()
            for j in range(i, i+k):
                if arr[j] < 0 :
                    q.append(arr[j])
            if not q:
                res.append(0)
            else:
                res.append(q.popleft())
            i+=1
        return res
