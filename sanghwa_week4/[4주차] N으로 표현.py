def solution(N, number):
    dp = [set() for i in range(8)]  # i 번 사용해서 만든 수 set()에 저장
    for i, x in enumerate(dp, 1):
        x.add(int(str(N) * i))
    for i in range(len(dp)):  # dp에 사칙연산 계산한 값 저장
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i - j - 1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add((op1 // op2))
        if number in dp[i]:
            answer = i + 1  # dp의 몇 번 쓰인 index를 리턴
            break  # 찾으면 반복 중지
        else:
            answer = -1
    return answer
