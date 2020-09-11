from collections import deque

def solution(n , m, image):
    answer = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                visited[i][j] = True
                bfs(n, m, i, j, image, visited)
                answer += 1
    return answer

def bfs(n, m, x, y, image, visited):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        DELTAS = ((0 ,1), (0, -1), (1, 0), (-1,0))
        for dx, dy in DELTAS:
            next_x = x + dx
            next_y = y + dy

            if valid_coord(next_x, next_y, n, m) and image[next_x][next_y] == image[x][y] and not visited[next_x][next_y]:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True

def valid_coord(x,y,n,m):
    return 0 <= x < n and 0 <= y < m



print(solution(2, 3 ,[[1, 2, 3], [3, 2, 1]]))