# Brute force o(n^2)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(len(gas)):
            curr_gas = gas[i]
            curr_index = i
            while curr_gas > 0 and curr_gas >= cost[curr_index]:
                curr_gas -= cost[curr_index]
                curr_index += 1
                curr_index = curr_index % n
                curr_gas += gas[curr_index]
                if curr_index == i:
                    return i
        return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1

        return res
