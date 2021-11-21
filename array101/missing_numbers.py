from typing import List

nums = [1, 2, 3, 3]
n = len(nums)
ret = []

def solution(nums) -> List[int]:
    count = 0

    for i in range(0, n):
        for j in nums:
            if count != 1:
                if nums[i] != j:
                    ret.append(i)
                    count += 1

    return ret

final = solution(nums)
print(final)
