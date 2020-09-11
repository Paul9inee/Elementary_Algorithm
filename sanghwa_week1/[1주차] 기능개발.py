import math
from _collections import deque

def solution(progresses, speeds):
    answer = []
    complete = 1
    finished = [math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]  # 종료 날짜 리스트
    finished_date = deque(finished)

    std_done = finished_date.popleft()
    for date in finished_date:
        if date <= std_done:
            complete += 1
        else:
            answer.append(complete)
            std_done = date
            # complete = 1
    answer.append(complete)
    return answer