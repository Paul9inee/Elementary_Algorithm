def solution(s, n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUWVXYZ"
    l_alpha = alpha.lower()
    answer = ''
    for letter in s:
        if letter.isspace() == True:
            answer = answer + " "
        elif letter.islower() == True:
            position = l_alpha.find(letter)
            newPosition = (position + n) % 26
            answer = answer + l_alpha[newPosition]
        else:
            position = alpha.find(letter)
            newPosition = (position + n) % 26
            answer = answer + alpha[newPosition]
    return answer

print(solution("AB", 1))
