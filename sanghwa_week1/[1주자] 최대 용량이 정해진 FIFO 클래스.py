class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size() + self.stack2.size() # 스택 2개로 이루어져있는 큐


    def push(self, item):
        if self.qsize() < self.max_size: # push 에 성공하면 true 리턴, 다만 원소 수가 최대 크기보다 작을때 가능하다
            self.stack1.push(item)
            return True
        else:
            return False

    def pop(self):
        try:
            if self.stack2.size() == 0: # stack2의 원소가 없으면 stack1에서 제거
                while self.stack1.size() > 0: # stack1이 비어있지 않을때, 수행한다
                    self.stack2.push(self.stack1.pop())
            result = self.stack2.pop()
        except IndexError: # 원소가 없으면 IndexError
            return False
        return result



n, max_size = map(int, input().strip().split(' '))
queue = MyQueue(max_size)

for _ in range(n):
    n_input = input().split()
    if "PUSH" in n_input:
        print(queue.push(n_input[1]))
    elif n_input[0] == "POP":
        print(queue.pop())
    elif n_input[0] == "SIZE":
        print(queue.qsize())