from itertools import combinations
def solution(nums):
    combi_nums = list(combinations(nums, 3))
    candidates = [sum(combi_num)for combi_num in combi_nums]
    primes = sieve(max(candidates))
    return len([candidate for candidate in candidates if candidate in primes])

def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for candidate in range(2, n+1):
        if not is_prime[candidate]:
                continue
        for multiple in range(candidate*candidate, n+1, candidate):
                is_prime[multiple] = False
    return [idx for idx, value in enumerate(is_prime) if value]

print(solution([1,2,3,4]))