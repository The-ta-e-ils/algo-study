def signs(l):
    if l == 1:
        return [[1], [-1]]
    
    result = []
    
    for sign in signs(l - 1):
        result.append(sign + [1])
        result.append(sign + [-1])
    
    return result

def solution(numbers, target):
    answer = 0
    
    num_signs = signs(len(numbers))
    
    for sign in num_signs:
        tmp_sum = 0
        
        for i in range(len(sign)):
            tmp_sum += sign[i] * numbers[i]
        
        if tmp_sum == target:
            answer += 1

    return answer
