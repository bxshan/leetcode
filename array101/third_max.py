from typing import List

nums = [1, 3, 2, 3, 4]

def solution(nums) -> List[int]:
    maximum = 0
    max_set = set()

    for i in range(3):
        maximum = 0
        for j in nums: 
            if j > maximum and (j not in max_set):
                maximum = j
        max_set.add(maximum)

    if maximum  == 0:
        return "nan"
    else:
        return maximum

final = solution(nums)
print(final)
