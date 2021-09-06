from typing import List

nums = [0, 123, -7213, 72, 909090, 1, 2321]


def solution(nums: List[int]) -> List[int]:
    even_nums = []

    for num in nums:
        original = num
        counter = 0
        while num != 0:
            num = int(num / 10)
            counter += 1
        if counter > 0 and counter % 2 == 0:
            even_nums.append(original)
    return even_nums


final = solution(nums)
print("The answer is: ", final)
