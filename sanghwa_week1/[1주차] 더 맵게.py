import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min_1 = heapq.heappop(scoville)
        if min_1 > K:
            break
        elif not scoville:
            answer = -1
            break
        min_2 = heapq.heappop(scoville)
        new_food = min_1 + (min_2 * 2)
        heapq.heappush(scoville, new_food)
        answer += 1
    return answer