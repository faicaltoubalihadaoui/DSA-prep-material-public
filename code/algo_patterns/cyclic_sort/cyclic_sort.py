# O (n) , nums contains numbers from the range of 1 to n
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[j] != nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums
