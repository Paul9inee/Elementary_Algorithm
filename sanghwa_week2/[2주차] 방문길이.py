def solution(dirs):
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    road = set()
    start = (0,0)

    for direction in dirs:
        dx, dy = directions[direction]
        next_x, next_y = start[0] + dx, start[1] + dy
        if (-5 <= next_x <= 5) and (-5 <= next_y <= 5):
            dstn = (next_x, next_y)
            road.add((start,dstn,dstn,start))
            road.add((dstn,start,start,dstn))

            start = dstn

    answer = len(road) / 2
    return answer