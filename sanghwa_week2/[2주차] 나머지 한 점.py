import collections
def solution(v):
    answer = []
    x_counter = dict(collections.Counter([x[0] for x in v]))  # x 좌표, 갯수대로
    y_counter = dict(collections.Counter([y[1] for y in v]))  # y 좌표, 갯수대로 

    answer.append(*[key for key in x_counter if x_counter[key] == 1])
    answer.append(*[key for key in y_counter if y_counter[key] == 1])
    return answer