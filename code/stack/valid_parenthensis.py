class Solution:
    def valid(self, s): 
        #code here
        stack = []
        hashm = { "{": "}", "[":"]", "(":")"}
        for i in s:
            if i in hashm.keys():
                stack.append(i)
            elif stack == [] or hashm.get(stack.pop()) != i:
                return False        
        return stack == []
