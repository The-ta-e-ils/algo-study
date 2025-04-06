def solution(matrix_sizes):
    n = len(matrix_sizes)  # 행렬 개수
    dp = [[float('inf')] * n for _ in range(n)]  # 최소 연산 횟수를 저장하는 DP 테이블

    # 자기 자신을 곱할 때, 연산 횟수는 0
    for i in range(n):
        dp[i][i] = 0

    # 행렬 곱의 길이를 2부터 n까지 늘려가며 최적의 곱셈 순서 찾기
    for size in range(2, n + 1):
        for start in range(n - size + 1):
            end = start + size - 1

            # 중간 분할 지점 mid를 설정하여 최소 연산 횟수 계산
            for mid in range(start, end):
                cost = (
                    dp[start][mid] + dp[mid + 1][end] +
                    matrix_sizes[start][0] * matrix_sizes[mid][1] * matrix_sizes[end][1]
                )
                dp[start][end] = min(dp[start][end], cost)

    return dp[0][n - 1]
