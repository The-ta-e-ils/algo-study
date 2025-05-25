# Use it with python3 boolYikes.py < input.txt
import sys
input = sys.stdin.read

def salutations():
    data = input().split() # flattened
    idx = 0 
    t = int(data[idx]) # num of cases
    idx += 1 # moving on
    results = []

    print(data)
    for _ in range(t):
        n = int(data[idx]) # num of nodes
        k = int(data[idx + 1]) # and k
        idx += 2 # read the content

        a = list(map(int, data[idx:idx + n])) # node values
        idx += n 

        # edge info bw nodes: tree init
        # inner lists stores neighbors
        edges = [[] for _ in range(n)]
        for _ in range(n - 1):
            # convert to 0 based
            u = int(data[idx]) - 1
            v = int(data[idx + 1]) - 1
            print(f"where am i: {data[idx]}, {data[idx+1]}")
            print(f"u, v: {u}, {v}")
            edges[u].append(v) # il vicino!
            edges[v].append(u) # la vicina! 🙄
            idx += 2
        print("-Tree-initialized-")

        # uncut total xor calculation
        total_xor = 0
        for val in a:
            total_xor ^= val

        # no point in processing it further-
        # -all sub comp will be 0 too when severed
        if total_xor == 0: 
            results.append("YES")
            continue
        
        # normal operation
        # DFS to find subtrees with XOR == total_xor
        # by finding two subcomps(trees) with the same total xor
        count = 0
        def dfs(node, parent):
            nonlocal count # limbo variable! 🚧 : not completely global
            current = a[node] # current node. this defines the 'cut'
            for neighbor in edges[node]: # for each child node
                if neighbor != parent: # do not go upstream you are not a salmon 🐟
                    current ^= dfs(neighbor, node) # add up the xor results
            
            # this component's total xor
            if current == total_xor:
                count += 1
                return 0 # no further counting for this comp -> cuz, self ^ 0 == self
            return current # if not, return result from this comp

        # from the top(root)
        dfs(0, -1)

        if count >= 2 and k >= 3:
            results.append("YES")
        else:
            results.append("NO")

        print("-E-N-D-O-F-C-A-S-E--------------------")
    print("\n".join(results))

salutations()