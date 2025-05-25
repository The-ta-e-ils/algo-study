# word conversion problem
from typing import List
def solution(begin: str, target: str, words: List[str]) -> int:
    """
    A search function.

    Args:
        begin (str): asdasd
        target (str): asdasd
        words (List[str]): asdasd
    
    Returns:
        int: The least number of operations to convert begin -> target
    """
    # one letter at a time
    # can only target the words that are in 'words'
    # -> meaning, swap with words that has ONE MISMATCHED letter
    def get_num_of_matches(w1: str, w2: str) -> int:
        return sum(1 for i, letter in enumerate(w1) if w2[i] != letter)
    
    # begin != target
    # universal word length 3 <= l <= 10, lower case
    # 3 <= len(words) <= 50 no dupe
    # return 0 if nothing can be converted

    # init deque with the [begin word, num of conversion, init record with 'begin']
    from collections import deque
    dq = deque([(begin, 0, {begin})])
    # init finished conversion records
    complete = set()
    
    # search
    while dq:
        # pop
        origin, num_of_conv, record = dq.popleft()
        print(f"inspecting {[origin, num_of_conv, record]}")
        # if match=word length -> add num of conversion to complete, break
        if origin == target:
            complete.add(num_of_conv)
            continue

        # loop 'words'
        for w in words:
            # clean record for each loop
            temp_rec = record
            temp_num = num_of_conv
            # count letter matches
            matches = get_num_of_matches(origin, w)
            # if match=1 and word is not in record -> add the word to queue, add the word to record, num of conv + 1, 
            if (matches == 1) and (w not in record):
                temp_rec.add(w)
                dq.append([w, temp_num + 1, temp_rec])
                print(f"word {w} added result: num of conv: {temp_num + 1}, added: {[w, temp_num + 1, temp_rec]}")
            # else: no match or too many matches or already in record -> deadend -> do nothing
        print(f"dq status: {dq}")
    if complete:
        return min(complete)
    return 0
