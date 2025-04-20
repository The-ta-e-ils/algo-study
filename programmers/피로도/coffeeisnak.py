from itertools import permutations


# 순서대로 정렬로는 최적해를 구할 수 없음. => 문제에 주어진 예시 자체가 단순 정렬(튜플형태, 대소 전환 포함)로는 안되었음.
# 시간 복잡도는 len(dun) = n 이라고 한다면
# O(n * n!) ~ O(n!)
# n <= 8이라서 가능 => 11개만 되도 >>> 4/3908/4800 => 4억번
def solution(k, dungeons):
    answer = 0
    permus = permutations(dungeons)

    for p in permus:
        cur_k = k
        cur_answer = 0
        for need, use in p:
            if cur_k >= need:
                cur_k -= use
                cur_answer += 1
        answer = max(cur_answer, answer)

    return answer
