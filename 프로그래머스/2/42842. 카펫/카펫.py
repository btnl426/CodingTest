
def solution(brown, yellow):
    answer = []
    for yellow_height in range(1, yellow+1):
        if yellow % yellow_height == 0:
            yellow_width = yellow // yellow_height

        if (yellow_width+2) * (yellow_height+2) - yellow == brown:
            return[yellow_width+2, yellow_height+2]