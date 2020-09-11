from collections import Counter
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
def solution(participant, completion):
    a = participant + completion
    return sorted(dict(Counter(a)).items(), key = lambda item: item[1])[-1][0]

print(solution(participant, completion))