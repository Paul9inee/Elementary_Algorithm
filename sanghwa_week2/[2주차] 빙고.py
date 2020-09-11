def solution(board, nums):
    bingo_dict = {} # 좌표 key 값 value
    N = len(board)

    for i in range(N):
        for j in range(N):
            val = board[i][j]
            bingo_dict[val] = (i, j)

    copy_map = [[0] * N for _ in range(N)]
    for num in nums:
        x = bingo_dict[num][0]  # 해당 dict value 의 x 좌표
        y = bingo_dict[num][1]  # 해당 dict value 의 y 좌표
        copy_map[x][y] = 1

    answer = 0

    cross1 = 0
    cross2 = 0

    for i in range(N):
        cross1 += copy_map[i][i]
        cross2 += copy_map[i][N-i-1]

    answer += cross1 == N
    answer += cross2 == N

    return answer +2