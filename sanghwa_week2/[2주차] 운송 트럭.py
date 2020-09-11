def solution(max_weight, specs, names):
    answer = 1
    accum = 0
    dict_specs = {key : int(value) for key, value in specs}
    for name in names:
        accum += dict_specs[name]
        if accum > max_weight:  # max_weight 가 넘어가면 ACCUM 초기화
            accum = 0
            accum += dict_specs[name]
            answer += 1
    return answer