### USING TWO POINTERS
def twoSum(self, numbers: list[int], target: int) -> list[int]:
    if not numbers:
        return None
    first, last = 0, len(numbers) - 1
    while first < last:
        current_sum = numbers[first] + numbers[last]
        if current_sum == target:
            return [first + 1, last + 1]
        elif current_sum < target:
            first += 1
        else:
            last -= 1
    return [-1, -1]


### USING HASH MAP
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        if not numbers:
            return None
        dictsum = {}
        for i in range(len(numbers)):
            e = target - numbers[i]
            if e in dictsum:
                return [dictsum[e] + 1, i + 1]
            else:
                dictsum[numbers[i]] = i
        return [-1, -1]
