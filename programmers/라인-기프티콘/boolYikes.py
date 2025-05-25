import re
from collections import Counter
def solution(code):
    cnt = Counter()
    for c in code:
        result = re.sub(r"[^a-zA-Z]","#" , c)
        cnt[result] += 1
    to_fix = dict(filter(lambda x: x[1] > 1, cnt.items()))
    return sum(to_fix.values())

cases = [
    [["AAA057", "AAA031", "BBB777"], 2],
    [["A0A12", "A1A23", "AA123", "BB123"], 2],
    [["A", "B"], 0],
    [["A1", "B1"], 0],
    [["A1", "A5"], 2]
]

for c in cases:
    answer = solution(c[0])
    assert answer == c[1], f"Wrong. The answer should be {c[1]}, not {answer}"
    print(f"Case {c} passed.")