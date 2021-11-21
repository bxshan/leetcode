from typing import List

nums = [1, 0]

def solution(nums) -> List[int]:
    i = 0
    j = len(nums) - 1
    while i < j:
        while nums[i] % 2 == 0:
            i += 1
        while nums[j] % 2 != 0:
            j -= 1
        if j > i: 
            tmp_i = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp_i
            print(i, j)
            print(nums)

    return nums

final = solution(nums)
print("the solution is:", final)
