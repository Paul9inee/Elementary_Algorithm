
def solution(brown, red):
    area = brown + red
    for height in range(3, area):
        width = area // height
        if (height - 2) * (width -2) == red and area == height * width:
            return [width, height]