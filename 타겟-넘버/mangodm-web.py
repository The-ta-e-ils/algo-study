from typing import List


def dfs(numbers: List[int], target: int, index: int=0, cum_sum: int=0) -> int:
    if index == len(numbers):
        return int(cum_sum == target)

    return (
        dfs(numbers, target, index + 1, cum_sum + numbers[index])
        + dfs(numbers, target, index + 1, cum_sum - numbers[index])
    )


def solution(numbers, target):
    return dfs(numbers, target)
