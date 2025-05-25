def solution(distance, rocks, n):
    # Sort rocks, add fin as the last rock
    rocks.sort()
    rocks.append(distance)

    # Binary search range
    left_most = 1
    right_most = distance
    answer = 0

    while left_most <= right_most:
        ## Guessing
        mid = (left_most + right_most) // 2
        removed = 0
        last_position = 0

        ## Check how many rocks need to be removed
        for rock in rocks:
            if rock - last_position < mid:
                removed += 1      # Distance too short, remove this rock
            else:
                last_position = rock       # Accept the rock

        ## Binary search update
        if removed > n:
            # Too many rocks removed, mid is too large
            right_most = mid - 1
        else:
            # Feasible, try for a larger minimum distance
            answer = mid
            left_most = mid + 1

    return answer

if __name__ == "__main__":
    cases = [[25, [2, 14, 11, 21, 17], 2, 4]]
    for case in cases:
        assert solution(*case[:3]) == case[3], f"wrong! should be {case[3]}"
        print(f"{case[3]} is correct!")
