# 행렬이 담긴 2차원 리스트가 주어지면 이를 이용해 최소 곱셈 연산 회수 리턴
# [a, b] [b, c] 행렬 둘의 곱은 a * b * c 이다.
def solution(matrices):
    answer = 0
    l = len(matrices)
    INF = float("inf")

    # dp[i][j] = i 번째 인덱스부터 j번째 인덱스까지의 행렬의 최소 곱셈 연산 회수
    # 당연히 j > i 여야 의미를 가짐.
    dp = [[0 for _ in range(l)] for _ in range(l)]

    # 역순 연산이 필요함! => i가 작아지면 연산 범위는 넓어짐! => 좁은 범위를 기반으로 줄여나갈 것
    # dp는 근본적으로 uppertriangular 이므로 맨 아래, 왼쪽부터 진행할 것임.
    # 최종 목표는 dp[0][l - 1]을 구하는 것
    for i in range(l - 1, -1, -1):
        for j in range(i + 1, l):  # i < j 인 경우 제외
            # 기본값을 초기화한담
            dp[i][j] = INF

            # 만약 j가 i + 1 이면 두 행렬을 그냥 곱합
            if j == i + 1:
                dp[i][j] = matrices[i][0] * matrices[j][0] * matrices[j][1]
                continue

            # i 번째 부터 j 번째 까지 행렬의 곱의 최소회수를 구하기 위해서 k를 도입, i ~ j - 1까지 이동하면서 양쪽을 나누는 기준이 됨.
            # 즉, i ~ k 까지의 행렬 곱의 최소 회수 + (k + 1) ~ j 까지 회수 + 두 행렬 곱하는 회수를 매번 비교
            for k in range(i, j):
                # kth_min은 k를 기준으로 양쪽으로 나눴을 때 최종 dp[i][j]의 후보가 되는 값
                kth_cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + matrices[i][0] * matrices[k + 1][0] * matrices[j][1]
                )
                dp[i][j] = min(dp[i][j], kth_cost)

    return dp[0][l - 1]
