from typing import List

nums = [0, 1, 2, 5, 4, 1]

def solution(nums) -> bool:
    increasing = True
    
    if len(nums) < 3:
        return False

    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i+1]:
            return False
        if nums[i] < nums[i+1] and increasing == False:
            return False
        if nums[i] > nums[i+1]:
            increasing = False
    return True

final = solution(nums)
print("the solution is:", final)
