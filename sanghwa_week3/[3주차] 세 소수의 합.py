from itertools import combinations
def solution(n):
    combi_primes = list(combinations(sieve(n), 3))
    # answer = [sum(combi_prime) for combi_prime in combi_primes]
    answer = list(map(sum, combi_primes))
    return answer.count(n)

def sieve(n):
    num = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
    return list(num)

print(solution(33))
