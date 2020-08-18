def solution(n):
    sum_l = []
    list = [i for i in range(1,n+1)]
    for i in list:
        if n % i == 0:
            sum_l.append(i)
    return sum(sum_l)

print(solution(12))