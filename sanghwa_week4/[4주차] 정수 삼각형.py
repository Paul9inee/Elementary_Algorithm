def solution(triangle):
    for row in range(1, len(triangle)):  # Root를 제외한 삼각형의 row. 1부터 시
        for idx in range(row + 1):       # Row의 idx
            if idx == 0:                 # 예외 처리, 1. 삼각형의 가장 왼쪽일 때 2. 가장 오른쪽일 때
                triangle[row][idx] += triangle[row - 1][0]
            elif idx == row:
                triangle[row][idx] += triangle[row - 1][-1]
            else:                        # 점화식, 왼쪽 대각선, 오른쪽 대각선으로 더한다.
                triangle[row][idx] += max(triangle[row - 1][idx - 1], triangle[row - 1][idx])
    return max(triangle[-1])
