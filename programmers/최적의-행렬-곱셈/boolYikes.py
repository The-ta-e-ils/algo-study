# itertools❎ sorting❎ search❎ dp✅
# divide by sub-problems
# big prob: where to split ? -> table[0][n-1] == min num of mult for Mat(1) to Mat(n)
# Chain mat mult cost formula : Cost(0~k) + Cost(k~n-1) + merge cost
def solution(sizes):

    n = len(sizes)

    # table[i][j] will store the minimum cost of multiplying Mat(i) to Mat(j)
    # j mats == j*j possible mult hence,
    table = [[0] * n for _ in range(n)] # so we don't compute the same thing ONONOA
    
    # optimal split
    # split = [[0] * n for _ in range(n)] # this is for returning the optimal position
    # mats mult chain (2 mats, 3 mats, ... n mats)
    for length in range(2, n + 1):
        
        # starting mats, diminishing
        for i in range(n - length + 1):
            
            # end of mult chain, incremental
            # length2: 0~1 1~2 2~3 3~4, length3: 0~2 1~3 2~4... ASO, ASF
            j = i + length - 1
            
            # this has a smaller footprint than sys.maxsize
            table[i][j] = float("inf")
            
            # split points 'k'
            for k in range(i, j):
                
                # this is where the formula kicks in
                # (first mat~splitter mats mult cost)
                # + (next to splitter~last mats mult cost)
                # + (first mat row x splitter mat col x last mat col = merge cost)
                cost = (
                    table[i][k]
                    + table[k+1][j]
                    + sizes[i][0] * sizes[k][1] * sizes[j][1]
                )

                if cost < table[i][j]:
                    table[i][j] = cost
                    # split[i][j] = k

    return table[0][n-1]