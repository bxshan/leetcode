from typing import List

nums = [1, 1, 1, 1, 1, 0, 1, 1, 0]


def solution(nums: List[int]) -> int:
    count = 0
    max_count = 0

    for i in nums:
        if i == 1:
            count += 1
        else:
            count = 0

        if count > max_count:
            max_count = count

    return max_count


answer = solution(nums)
print("The answer is: ", answer)
