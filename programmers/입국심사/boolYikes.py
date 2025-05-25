def solution(n, times):
    left = 0
    right = max(times) * n # worst case
    res = right

    while left <= right:
        mid = (left + right) // 2
        tasks_done = sum(mid // t for t in times)
        # print(f"|{left}|{mid}|{right}, tasks done: {tasks_done}", end=" ")

        if tasks_done >= n:
            res = mid
            right = mid - 1
            # print(f">= {n}, res = {mid}, right = {mid - 1}")
        else:
            left = mid + 1
            # print(f"< {n}, res stays same, left = {mid + 1}")
    
    return res