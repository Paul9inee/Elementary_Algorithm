def solution(s):
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0