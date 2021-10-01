from typing import List

nums = [1, 9, 9, 3, 8, 7, 0]


def solution(nums: List[int]) -> List[int]:
    result = []
    for i in nums:
        result.append(i * i)

    print('the new array: ', result)

    for p in range(len(result) - 1):
        for q in range(len(result) - 1 - p):
            print('comparing: ', result[q], result[q+1])
            if result[q] > result[q+1]:
                result[q], result[q+1] = result[q+1], result[q]   
        print('the new array: ', result)
    return result

answer = solution(nums)
print("the answer is ", answer)
