from typing import List

nums = [1, 2, 2, 3, 3, 4, 5, 6, 6]

def solution(nums) -> List[int]:
    current = 0
    counter = 0
    i = 0
    original_len = len(nums)

    while counter < original_len:
        counter += 1

        if current == nums[i]:
            # nums.pop(i)
            for j in range(i + 1, i + 1 + original_len - counter):
                nums[j - 1] = nums[j]
        else:
            current = nums[i]
            i += 1

    return nums

final = solution(nums)

print("the answer is: ", final)
