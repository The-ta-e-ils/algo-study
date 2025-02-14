def solution(numbers, target):
    # 결과 개수, 초기 0
    count = 0

    def dfs(i, s):
        nonlocal count
        # 숫자 다 썼으면
        if i == len(numbers):
            if s == target:  # 목표 달성?
                count += 1
            return
        # 현재 숫자 더하기
        dfs(i + 1, s + numbers[i])
        # 현재 숫자 빼기
        dfs(i + 1, s - numbers[i])
    
    # DFS 시작
    dfs(0, 0)
    return count
