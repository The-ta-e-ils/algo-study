from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0  # 변환할 수 없는 경우
    
    def can_change(a, b):
        # 한 글자만 다른지 체크
        return sum(x != y for x, y in zip(a, b)) == 1

    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        word, steps = queue.popleft()
        if word == target:
            return steps
        
        for next_word in words:
            if next_word not in visited and can_change(word, next_word):
                visited.add(next_word)
                queue.append((next_word, steps + 1))
    
    return 0  # 변환할 수 없는 경우
