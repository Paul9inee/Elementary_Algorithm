def solution(s):
    stack = []
    for alphabet in s:
        if stack and stack[-1] == alphabet:
            stack.pop()
        else:
            stack.append(alphabet)
    if stack: return 0
    else: return 1
