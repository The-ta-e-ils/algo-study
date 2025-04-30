def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    idx_map = {ch: i for i, ch in enumerate(vowels)}
    total = 0
    for i, ch in enumerate(word):
        ch_index = idx_map[ch]
        # 뒤에 남은 자릿수에서 만들 수 있는 조합 수
        for j in range(i, 5):
            total += ch_index * (5 ** (4 - j))
        total += 1  # 현재 단어 자체
    return total
