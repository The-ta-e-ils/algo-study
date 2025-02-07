def solution(brown, yellow):
    for y_height in range(1, int(yellow**(1/2))+1):
        if yellow % y_height == 0:
            y_width = yellow // y_height
            if brown == y_width*2 + y_height*2 + 4:
                return [y_width+2, y_height+2]
