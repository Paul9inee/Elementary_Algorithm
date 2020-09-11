stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3


def solution(stones, k):
    count = 0
    while True:
        count += 1
        for i in range(len(stones)):
            if stones[i] != 0:
                stones[i] -= 1

    return count


print(solution(stones, k))