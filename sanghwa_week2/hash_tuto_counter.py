sentence = "demi is very very lazy"
import collections
def solution(sentence):
    my_counter = dict(collections.Counter(sentence.split(" ")))
    counted = sorted(my_counter.items(), key=lambda x:-x[1])
    return counted[0][0]

print(solution(sentence))
