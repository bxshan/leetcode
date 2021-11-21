from typing import List

num1 = [1, 2, 4, 0, 0, 0]
num2 = [1, 2, 3]
m = 3
n = 3
def solution(num1, num2, m, n) -> List[int]:
    i = 0
    j = 0
    count = 0

    while count < n:
        print("num1: ", num1)
        if num2[j] <= num1[i]:
            for l in range (m + count - 1, i - 1, -1):
                print(l)
                num1[l+1] = num1[l]
            num1[i] = num2[j]
            print("after : ", num1)

            j += 1
            i += 1
            count += 1
        else:
            i += 1

    return num1

final = solution(num1, num2, m, n)

print("the answer is: ", final )
