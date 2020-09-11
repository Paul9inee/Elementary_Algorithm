def solution(s):
    answer = []
    for i in range(len(s)):
        for j in range(1, len(s) + 1):
            if s[i:j] and str(s[i:j]) == str(s[i:j])[::-1]:
                answer.append(s[i:j])
            elif s[j:i] and str(s[j:i]) == str(s[j:i])[::-1]:
                answer.append(s[j:i])
    return max(answer)
print(solution("abcdbda"))