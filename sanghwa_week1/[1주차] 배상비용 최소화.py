import heapq
def solution(no, works):  # max heap 만들기
    works = [-1 * x for x in works]  # min heap으로만 되어있기 떄문에 음수로 변환한다

    heapq.heapify(works)

    while no != 0:
        max_val = heapq.heappop(works)
        if max_val == 0:
            break
        heapq.heappush(works, max_val + 1)
        no -= 1

    return sum([i ** 2 for i in works])

# 정렬 자료구조를 이용하면 시간 복잡도 통과 못함
# heap을 이용하면 O(NlogN)