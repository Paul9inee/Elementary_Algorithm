# 튜플만으로 구현
def solution(seat):
    ticket = set([(x,y) for x, y in seat])
    return len(ticket)

# map과 튜플로 구현
# def solution(seat):
#     ticket = set((map(tuple ,seat)))
#     return len(ticket)
