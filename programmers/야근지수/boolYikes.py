import heapq

# Reducing the biggest workload contributes to the least amount of sum of fatigue in the end
# Greedy + heap
def solution(n, works):
    # Max-heap to track the most stressful (largest) work first.
    # Python's heapq is a min-heap, so we push negative values to simulate a max-heap.
    mx_heap = []

    # Total fatigue is initially the sum of squares of all work amounts.
    fatigue = 0
    for w in works:
        heapq.heappush(mx_heap, -w)  # Push negated work into the heap (max-heap behavior)
        fatigue += w**2              # Sum of squares of work loads (initial fatigue)

    # Reduce the largest work unit `n` times
    for _ in range(n):
        stressige_arbeit = -heapq.heappop(mx_heap)  # Get the largest work unit (restore to positive)
        if stressige_arbeit < 1:
            break  # No more work to reduce

        # Remove current work's fatigue contribution
        fatigue -= stressige_arbeit ** 2
        # Reduce the most stressful work by 1
        stressige_arbeit -= 1
        # Add new reduced fatigue contribution
        fatigue += stressige_arbeit ** 2
        # Push the updated work back into the heap
        heapq.heappush(mx_heap, -stressige_arbeit)

    # Return total fatigue after all reductions
    return fatigue
