def solution(nambaz, target):
    # Uniiiiiiiiiiiiique records
    rec = set()
    stk = [(0, 0, tuple())] # sum, idx, path
    num_len = len(nambaz)
    while stk:
        # pop from the last of the LAST -> Deep Kimchi Search
        curr = stk.pop()
        # print(curr)
        # end of the line == none left out
        if curr[1] == num_len:
            # & overshot -> do nothing
            if curr[0] > target: 
                continue
            # & bullseye -> add to the hashset
            if curr[0] == target:
                rec.add(curr[2])
            # & under -> do nothing
            continue
        # hasn't reached num_len yet -> 
        stk.append((curr[0] + nambaz[curr[1]], 
                    curr[1] + 1, 
                    curr[2] + (nambaz[curr[1]],)
                    )) # addition path
        stk.append((curr[0] + (nambaz[curr[1]] * -1), 
                    curr[1] + 1, 
                    curr[2] + ((nambaz[curr[1]] * -1),)
                    )) # subtraction path
        # are both added to the LAST of the stack
    return len(rec)