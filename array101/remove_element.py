from typing import List

nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
element = 1

def solution(nums) -> List[int]:
    i = 0
    count = 0
    deleted = 0
    length = len(nums)
    while count < length:
        count += 1
        if nums[i] == element:
            for j in range (i+1, length-deleted):
                nums[j-1] = nums[j]
            nums[-1-deleted] = 0
            deleted += 1
        else:
                i += 1
                
    return nums

final = solution(nums)
print("the solution is:", final)
