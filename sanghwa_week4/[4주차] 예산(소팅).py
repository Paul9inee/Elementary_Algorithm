def solution(demands, budget):
    answer = []
    demands.sort()
    for demand in demands:
        budget -= demand
        answer.append(demand)
        if budget < min(demands):
            break
    return answer

print(solution([1,3,2,5,4],9))