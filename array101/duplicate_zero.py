from typing import List

nums = [1, 0, 4, 0, 0, 5, 0, 9]

def solution(nums) -> List[int]:
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.append(0)

            for j in range(len(nums) - 1, i, -1):
                nums[j] = nums[j - 1]
                 
            i += 1

        i += 1

    return(nums)

answer = solution(nums)
print("the answer is ", answer)
