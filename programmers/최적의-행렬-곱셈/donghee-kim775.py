"""
크기가 a by b인 행렬과 크기가 b by c 인 행렬이 있을 때, 
두 행렬을 곱하기 위해서는 총 a x b x c 번 곱셈해야합니다.
예를 들어서 
A = 5 by 3인 행렬과 
B = 3 by 2인 행렬을 
곱할 때) 는 총 5 x 3 x 2 = 30번의 곱하기 연산을 해야 합니다.
=> 행렬이 2개일 때는 연산 횟수가 일정 하지만, 

행렬의 개수가 3개 이상일 때는 연산의 순서에 따라서 곱하기 연산의 횟수가 바뀔 수 있습니다. 
예를 들어서 
A = 크기가 5 by 3인 행렬, 
B = 크기가 3 by 10인 행렬 B, 
C = 크기가 10 by 6인 행렬 C가 있을 때, 
순서대로 A와 B를 먼저 곱하고, 그 결과에 C를 곱하면 A와 B행렬을 곱할 때 150번을, 
AB 에 C를 곱할 때 300번을 연산을 해서 총 450번의 곱하기 연산을 합니다. 

하지만, B와 C를 먼저 곱한 다음 A 와 BC를 곱하면 
180 + 90 = 270번 만에 연산이 끝납니다.

각 행렬의 크기 matrix_sizes 가 매개변수로 주어 질 때, 모든 행렬을 곱하기 위한 최소 곱셈 연산의 수를 return하는 solution 함수를 완성해 주세요.

제한 사항
행렬의 개수는 3이상 200이하의 자연수입니다.
각 행렬의 행과 열의 크기는 200이하의 자연수 입니다.
계산을 할 수 없는 행렬은 입력으로 주어지지 않습니다.

matrix_sizes = [[5,3],[3,10],[10,6]] # => 270
"""

# 방법 1..? 리스트를 한 리스트로 풀고 리스트 네개짜리를 윈도우형식으로 삼아 최대값들 비교..?해서 없애가면서 숫자 세개 남으면 반복문 그만..?
# 1. 5 3 3 10 10 6 => 10 먼저 없애고 합 answer에 연산횟수 플러스..?
# 2. 5 3 3 10 10 6 => set으로 중복 제거하고 => 5 3 10 6 => 큰 제일 처음과 끝 제외 중간에서 가장 큰 숫자들을 뽑아가며 양 옆 곱해서 연산..? 중복된 숫자가 있다면...?
# 1번을 하든 2번을 하든 [5, 10], [10, 7], [7, 10], [10, 6] => 5 10 7 10 6 =>

# 혹은 3개 씩 묶어서 곱한 것을 리스트에 넣고 가장 높게 나온 것을 answer에 더하고 해당 list 위치 값 제거 후 또다시 반복...?
# => 시간 복잡도....
def solution(matrix_sizes):
    total_list = []
    matrix_sizes_len = len(matrix_sizes)
    if matrix_sizes_len == 2:
        answer = matrix_sizes[0][0] * matrix_sizes[0][1] * matrix_sizes[1][1]
        return answer
    
    for i in matrix_sizes:
        total_list.append(matrix_sizes[i][0])
        total_list.append(matrix_sizes[i][1])
    # 1번 방법
    for i in range(0, matrix_sizes_len-1):
        print(total_list[i*2:i*2+4])
    
    # 2번 방법
    total_list = list(set(total_list))    
    
    answer = 0

    return answer