from collections import defaultdict
from collections import deque

class Gurafu:
    def __init__(self):
        self.nodes = defaultdict(list)
    # def get_node(self, node_num):
    #     return self.nodes[node_num]
        # return list(map(lambda node: node.number == node_num, self.nodes))[0]
    def add_node(self, k, v):
        self.nodes[k].append(v)
        self.nodes[v].append(k) # bidirectional

def solution(n, edges):
    # init tree
    g = Gurafu()
    for edge in edges:
        g.add_node(edge[0], edge[1])

    # BFS guarantees shortest path ... right? 🥺
    distances = {}
    dq = deque([(0, 1)]) # dist, node

    while dq:
        dist, node = dq.popleft()
        if node in distances:
            continue
        distances[node] = dist
        for neighbor in g.nodes[node]:
            if neighbor not in distances:
                dq.append((dist + 1, neighbor))

    max_dist = max(distances.values())
    print(max_dist)
    return [node for node, dist in distances.items() if dist == max_dist]
