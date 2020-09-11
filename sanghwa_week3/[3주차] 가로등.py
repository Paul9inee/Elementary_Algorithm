import math
# 그리디
def solution(l, v):
    v.sort()
    distance = []
    for lamp1, lamp2 in zip(v[1:], v[:-1]):  # 가로등 사이의 거리로 /2 한 것이 불빛의 길이 d.
        d = math.ceil((lamp1 - lamp2) / 2)
        distance.append(d)
    distance += [v[0], l - v[-1]]  # 첫 번째, 마지막 가로등 추가
    return max(distance)  # 가장 긴 길이로 도로를 가려야함.

# 이진탐색

def solution(l ,v):

    return

