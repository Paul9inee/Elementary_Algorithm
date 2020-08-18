def solution(arr, divisor):
    list = []
    for x in arr:
        if x % divisor == 0:
            list.append(x)
        elif len(list) == 0:
            list.append(-1)
            return list
    return list
