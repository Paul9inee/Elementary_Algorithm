# 모서리에 위치하면 안됨
from collections import deque
from itertools import combinations

def solution(n):
    answer = 0
    visited = [[False] * n for _ in range(n)]
    chess = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                bfs(n, visited, chess)
                answer += 1
    return answer

def quenn_conquer(x, y, n, chess):
    for i in range(n):
        for j in range(n):
            chess[i][y] += 1  # 가로
            chess[x][j] += 1  # 세로
            chess[i+1][j+1] += 1  # 대각
            return chess

def bfs(n, visited, chess):
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dx, dy in DELTAS:
            next_x = x + dx
            next_y = y + dy


            if valid_coord(n, next_x, next_y) and not visited[next_x][next_x] and chess[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True
                chess[next_x][next_y] = chess[x][y] + 1

                return

def valid_coord(n, x, y):
    return 0 <= x <= n and 0 <= y <= n

print(solution(4))