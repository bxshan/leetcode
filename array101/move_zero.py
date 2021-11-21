from typing import List

nums = [1, 0, 11, 0, 111]

def solution(nums) -> List[int]:
    i = 0
    j = 0
    
    while nums[i] != 0:
        i += 1
        j += 1

    while i < len(nums):
        while i < len(nums) and nums[i] == 0:
            if i == len(nums) - 1:
                return nums
            i += 1
        while j < len(nums) and nums[j] != 0:
            j += 1 

        print(i, j)
        tmp_i = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp_i

        print(nums)

    return nums

final = solution(nums)
print("the solution is:", final)
