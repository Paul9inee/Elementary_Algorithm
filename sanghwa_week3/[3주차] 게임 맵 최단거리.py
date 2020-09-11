from _collections import deque
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]  # 방문했는지 check
    traveled = [[1] * m for _ in range(n)]  # 이동한 거리, 매번 check
    bfs(n, m, maps, visited, traveled)

    return traveled[n - 1][m - 1] if traveled[n - 1][m - 1] != 1 else -1  # traveled의 마지막 값 리턴


def bfs(n, m, maps, visited, traveled):
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True

    WALL, ROAD = 0, 1

    while queue:
        x, y = queue.popleft()

        DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dx, dy in DELTAS:
            next_x = x + dx
            next_y = y + dy

            if valid_coord(next_x, next_y, n, m) and not visited[next_x][next_y] and maps[next_x][next_y] == ROAD:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True
                traveled[next_x][next_y] = traveled[x][y] + 1

                if next_x == n - 1 and next_y == m - 1:
                    return


def valid_coord(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))