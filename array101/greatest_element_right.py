from typing import List

nums = [1, 2, 3, 2]

def solution(nums) -> List[int]:
    for i in range(0, len(nums)):
        maximum = 0
        for j in range (i+1, len(nums)):
            if nums[j] > maximum:
                maximum = nums[j]

        nums[i] = maximum
         
    nums[-1] = -1
    
    return nums

def solution2(nums) -> List[int]:
    maximum = -1
    right = nums[-1]

    for i in range(len(nums)-2, -1, -1):
        maximum = max(right, maximum)
        right = nums[i]
        nums[i] = maximum

    nums[-1] = -1

    return nums

# final = solution(nums)
final2 = solution2(nums)

# print(final)
print(final2)

