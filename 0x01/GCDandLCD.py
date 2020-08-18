import math
def solution(n, m):
    a = math.gcd(n,m)
    b = n * m //(a)
    return [a,b]