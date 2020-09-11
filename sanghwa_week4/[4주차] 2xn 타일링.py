def solution(n):
    tile1, tile2 = 1, 1
    for i in range(n):
        tile1, tile2 = tile2, tile1 + tile2
    return tile1 % 1000000007
