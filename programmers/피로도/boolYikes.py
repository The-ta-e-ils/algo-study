# len(dungeons) <= 8, not a crazy number
# -> perm is good to go 🤓
from itertools import permutations
def solution(k, dungeons):
    # k = a quel point fatigue
    # [[80,20],[50,40],[30,10]]
    n = range(len(dungeons))
    
    # index permutations
    perm = permutations(n)
    done = set()
    
    for p in perm:
        curr = k
        trav = tuple()
        for i in p:
            if dungeons[i][0] <= curr:
                curr -= dungeons[i][1]
                trav += (i,)
            else:
                break
        done.add(trav)
    res = max(done, key=lambda x: len(x))
    return len(res)