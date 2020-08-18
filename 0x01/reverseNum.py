def solution(n):
    ls = list(map(int, str(n)))
    return ls[::-1]


print(solution(1283))