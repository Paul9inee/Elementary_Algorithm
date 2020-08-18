a,b,c = map(int, input().split())
abc = [a, b,c]
abc.sort()
for i in range(3):
    print(abc[i])