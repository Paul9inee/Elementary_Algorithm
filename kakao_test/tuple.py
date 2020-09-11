s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"

def mk_list(s):
    list = []
    s = s[1:-1]
    for i in range(len(s)):
        if s[i] == '{':
            while s[i] == '}':
                list.append(s[i+1])
    return list

mk_list(s)

