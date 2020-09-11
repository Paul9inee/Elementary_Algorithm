def solution(no, works):
    while no != 0:
        works.sort(reverse = True)
        works[0] -= 1
        no -= 1
    for i in range(len(works)):
        works[i] = works[i] ** 2
    return sum(works)