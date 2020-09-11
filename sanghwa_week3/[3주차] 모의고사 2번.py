# 1. 아파트에 모두 설치한다.
# 2. wified에 0이 있기전까지 지운다.
# 3. 초기 station 만 설치 되어있을때랑 비교한다.
import math
def solution(n, stations, w):
    answer = 0
    wified = 0
    freq = (w * 2 + 1)
    for station in stations:
        lower = station - w
        upper = station + w
        if wified <= lower:
            answer += math.ceil((lower - 1 - wified) / freq)
        wified = upper
    if wified <= n:
        answer += math.ceil((n - wified) / freq)
    return answer


print(solution(11, [4,11], 1))

