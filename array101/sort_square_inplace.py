from typing import List

nums = [-2, 3, 4, 1, 9, 7, -8, -6]

def solution(nums) -> List[int]:
    for k in range(len(nums)): 
        nums[k] = nums[k]*nums[k]

    for i in range(len(nums)-1):  
        for j in range(len(nums) - 1 -i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

final = solution(nums)
print(final)
