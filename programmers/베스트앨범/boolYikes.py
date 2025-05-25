from collections import Counter, defaultdict

def solution(genres, plays):
    cnt = Counter()
    for g, p in zip(genres, plays):
        cnt[g] += p
    # print(f"Genres played: {cnt}")
    
    cnt_sorted = list(map(lambda x: x[0], sorted(cnt.items(), reverse=True, key=lambda x: x[1])))
    # print(f"Genre played sorted: {cnt_sorted}")
    
    rank = defaultdict()
    for i, g in enumerate(cnt_sorted):
        rank[g] = i
    # print(f"Genre chart: {rank}")
    
    rank_mapped = list(map(lambda x: rank[x], genres))
    # print(f"Genres mapped to ranks: {rank_mapped}")
    
    res = []
    for i, info in enumerate(zip(rank_mapped, plays)):
        # index, genre rank, times played
        res.append((i, info[0], info[1]))
        cnt[info[0]] += 1
    # print(f"All info in one: {res}")
    
    cnt = Counter()
    def cust_mapper(x):
        # if it already has 2 of the kind, pass
        idx, rank, played = x
        if cnt[rank] < 2:
            cnt[rank] += 1
            return idx
        
    res = sorted(res, key=lambda x: (x[1], -x[2], x[0]))
    # print(f"Info sorted by criteria: {res}")
    # print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-")
    
    return list(filter(lambda x: x is not None, map(cust_mapper, res)))