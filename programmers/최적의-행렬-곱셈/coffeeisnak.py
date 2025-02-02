def solution(matrices):
    l = len(matrices)

    # dp[i][j] = 리스트 인덱스 기준으로 i 번째 부터 j번째 까지의 행렬을 곱할 때 최소 연산 회수
    dp = [[0] * l for _ in range(l)]
    
    # i부터 j까지의 행렬을 곱하므로, 더 좁은 범위의 최소값이 주어져야 해서 행은 역순으로 반복문을 계산
    # 2 부터 4까지 2 3 3 4 
    for j in range(l):
        for i in range(l - 1, -1, -1):
            if j <= i:  # 결국 정사각형으로 보면 위쪽, 오른쪽 삼각형만 채우는거
                continue
            
            # 초기값 설정
            dp[i][j] = float("inf")
            for k in range(i, j):
                # 행렬의 곱셈은 교환법칙이 일반적으로 성립하지 않으므로, k를 i부터 j - 1까지 변경하며 
                # 양쪽으로 나눈 행렬들의 최소값을 기준으로 시작하여 최소 연산 회수를 탐색
                cur_result = dp[i][k] + dp[k + 1][j] + (matrices[i][0] * matrices[k][1] * matrices[j][1])
                dp[i][j] = min(dp[i][j], cur_result)

    return dp[0][l - 1]
