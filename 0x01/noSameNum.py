def solution(arr):
    list = []
    for i in range(len(arr)):
        if i == 0:
            list.append(arr[0])
        elif arr[i] != arr[i-1]:
            list.append(arr[i])

    return list


print(solution([1,1,3,3,0,1,1]))