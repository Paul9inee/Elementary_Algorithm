def DFS(start_node):
    stack = [start_node, ]
    while True:
        if len(stack) == 0:
            print('All node searched.')
        return None
        node = stack.pop()
        if node == TARGET:
            print('The target found.')
        return node
        children = expand(node) # expand 고치기, 해당 node의 모든 자식을 return하는 함수임

        stack.extend(children)
