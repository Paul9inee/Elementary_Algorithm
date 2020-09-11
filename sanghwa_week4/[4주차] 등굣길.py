def solution1(m, n, puddles):
    traveled = [[0] * m for _ in range(n)]
    traveled[0][0] = 1
    for row in range(n):
        for idx in range(m):
            if row == 0 and idx == 0:
                continue
            if [idx+1,row+1] in puddles:
                traveled[row][idx] = 0
            else:
                traveled[row][idx] = traveled[row][idx - 1] + traveled[row - 1][idx]
    return traveled[n - 1][m - 1] % 1000000007
print(solution1(4, 3, [[2,2]]))