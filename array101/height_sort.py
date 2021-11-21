from typing import List

nums = [1, 5, 1, 3, 4, 2]

def solution(nums) -> int:
    correct = nums.copy()
    count = 0

    for i in range(0, len(correct)):
        for j in range(i+1, len(correct)):
            if correct[i] > correct[i+1]:
               tmp = correct[i] 
               correct[i] = correct[i+1]
               correct [i+1] = tmp

    for i in range(0, len(nums)):
        if nums[i] != correct[i]:
            count += 1

    print("the original list: ", nums)
    print("the sorted list: ", correct)

    return count

final = solution(nums)
print("the solution is:", final)
