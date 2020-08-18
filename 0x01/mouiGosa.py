def solution(answers):
    answer = []
    p_supo1 = [1, 2, 3, 4, 5]
    p_supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p_supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == p_supo1[i % len(p_supo1)]:
            scores[0] += 1
        elif answers[i] == p_supo2[i % len(p_supo2)]:
            scores[1] += 1
        elif answers[i] == p_supo3[i & len(p_supo3)]:
            scores[2] += 1
    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1)


    return answer