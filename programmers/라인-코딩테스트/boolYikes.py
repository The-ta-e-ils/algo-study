# from functools import lru_cache
from itertools import combinations_with_replacement, product

def solution(problems):
    possibilities = []
    for p in problems:
        score_alloc, n_cases = p
        raw_comb = combinations_with_replacement(range(1, score_alloc + 1), n_cases)
        filtered = list(filter(lambda x: sum(x) == score_alloc, raw_comb))
        this_problem = []
        for stuff in filtered:
            this_problem.append(bin_comb(stuff))
        possibilities.append(this_problem)
    
    outcomes = []
    for p in product(*possibilities):
        outcomes.append(sum_comb(p))
    
    return max(map(lambda x: len(x), outcomes))

def bin_comb(stuff):
    """Make a product of (0, 1) and the input, essentially forming a list of possible scores"""
    n = len(stuff)
    results = []
    for binary in product([0, 1], repeat=n):
        prod = sum(v * b for v, b in zip(stuff, binary))
        results.append(prod)
    return results

def sum_comb(stuff):
    """Generate all possible sums by choosing one score from each subset"""
    result = set()

    def dfs(i, total):
        if i == len(stuff):
            result.add(total)
            return
        for val in stuff[i]:
            dfs(i + 1, total + val)
    
    dfs(0, 0)
    # if i == len(stuff):
    #     return possible_scores
    
    # if i == 0:
    #     possible_scores = stuff[i]
    
    # for a in set(possible_scores):
    #     for b in stuff[i+1]:
    #         possible_scores.append(a + b)
    
    # i += 1

    # if i + 1 == len(stuff):
    #     return possible_scores
    
    # return sum_comb(stuff, i, possible_scores)    
    return result

problems = [
    [[[6, 2], [4, 2]], 11],
]
for p in problems:
    answer = solution(p[0])
    correct = p[1]
    assert answer == correct, f"Wrong! Expected {correct}"
    print(f"Answer {answer} is correct!")