def solution(info, n, m):
    # init
    min_tracker = float('inf')
    records = set()

    dfs(0, 0, 0, info, n, m, records, min_tracker)

    return min_tracker if min_tracker != float('inf') else -1

def dfs(index, a_sum, b_sum, info, n, m, records, min_tracker):
    # Don't get caught
    if a_sum >= n or b_sum >= m:
        return

    # Skip the visited ones
    if (index, a_sum, b_sum) in records:
        return
    records.add((index, a_sum, b_sum))

    # If we've considered all items
    if index == len(info):
        min_tracker = min(min_tracker, a_sum)
        return

    a_trace, b_trace = info[index]

    # Option 1: assign to A
    dfs(index + 1, a_sum + a_trace, b_sum, info, n, m, min_tracker)
    # Option 2: assign to B
    dfs(index + 1, a_sum, b_sum + b_trace, info, n, m, min_tracker)