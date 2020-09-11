sentence = "demi is very very lazy"
def solution(sentence):
    words = sentence.split(" ")
    my_counter = {}
    for word in words:
        my_counter[word] = my_counter.get(word, 0) + 1  # word를 key로 받아서 item 삽입
    counted = sorted(my_counter.items(), key=lambda x:-x[1])
    return counted[0][0]

print(solution(sentence))