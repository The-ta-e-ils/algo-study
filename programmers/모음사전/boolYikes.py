def solution(word):
    VOW = "AEIOU"
    cnt = 0
    for v in VOW:
        cnt += 1
        if v == word: return cnt
        for o in VOW:
            cnt += 1
            if f'{v}{o}' == word: return cnt
            for w in VOW:
                cnt += 1
                if f'{v}{o}{w}' == word: return cnt
                for e in VOW:
                    cnt += 1
                    if f'{v}{o}{w}{e}' == word: return cnt
                    for l in VOW:
                        cnt += 1
                        if f'{v}{o}{w}{e}{l}' == word: return cnt
    return -1