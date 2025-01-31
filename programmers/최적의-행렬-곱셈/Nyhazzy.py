def solution(matrix_sizes):
    length = len(matrix_sizes)
    # dp 테이블 생성, dp[i][j]는 행렬 i부터 j까지 곱하는 최소 곱셈 횟수
    dp = [[0 for _ in range(length)] for _ in range(length)]
    
    # 행렬 곱셈 범위 길이를 기준으로 DP 계산
    for gap in range(1, length):  # gap은 곱할 행렬의 범위 길이
        for start in range(0, length - gap):  # start는 행렬 범위의 시작 인덱스
            end = start + gap  # end는 행렬 범위의 끝 인덱스
            
            # 중간 인덱스를 기준으로 분할하여 최소 곱셈 횟수를 계산
            dp[start][end] = float('inf')  # 최소값을 찾기 전에 먼저 무한대로 초기화
            for mid in range(start, end):
                # dp[start][mid] + dp[mid+1][end] + 계산된 연산 횟수
                dp[start][end] = min(
                    dp[start][end],
                    dp[start][mid] + dp[mid + 1][end] + matrix_sizes[start][0] * matrix_sizes[mid][1] * matrix_sizes[end][1]
                )
    
    return dp[0][length - 1]  # 최종 결과는 dp[0][length-1]에 저장됨