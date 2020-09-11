s= "xyb"

def solution(s):
    stack = []
    for string in s:
        while stack and stack[-1] < string:
            stack.pop()
        stack.append(string)
    return ''.join(stack)
print(solution(s))
