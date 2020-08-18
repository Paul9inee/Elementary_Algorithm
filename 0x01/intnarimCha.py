# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))

def solution(n):
    l = list(str(n))
    l.sort(reverse=True)
    return int("".join(l))


print(solution(8838123))