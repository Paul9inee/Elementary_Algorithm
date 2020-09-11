def solution(s):
    pair = {')' : '(', ']' : '[', '}' : '{'}
    stack = []
    for bracket in s:
        if bracket not in pair:
            stack.append(bracket)
        # elif bracket in pair:
        elif stack and stack[-1] == pair[bracket]:
            stack.pop()
        else:
            return False
    return len(stack) == 0

# def solution(s):
#     stack = []
#     for bracket in s:
#         if bracket in '{[(':
#             stack.append(bracket)
#         elif bracket == '}':
#             if stack and stack[-1] == '{':
#                 stack.pop()
#             else:
#                 return False
#         elif bracket == ')':
#             if stack and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 return False
#         elif bracket == ']':
#             if stack and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0