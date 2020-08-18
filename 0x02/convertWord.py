answer = 0
def dfs(begin, target, words, visited):
    global answer
    stacks = [begin]
    while stacks:
        stacks.pop()
        stack = stacks.pop()
        if begin == target:
            return answer
        for w in range(len(words)):
            if [] == 1:
                answer += 1

def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [0 for i in words]
    global answer
    return answer