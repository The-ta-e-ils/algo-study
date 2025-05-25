# nerd power index prob
def solution(citations):
    target = 0
    candid = []
    mx = max(citations)
    while target <= mx:
        m = list(map(lambda x: x >= target, citations))
        # print(target, sum(m)) # map and filter are consummables!
        if sum(m) >= target:
            others = [e for e, b in zip(citations, m) if not b]
            if sum(map(lambda x: x <= target, others)) == len(others):
                candid.append(target)
        target += 1
    return max(candid)