# shortest route search
# def solution(maps):
#     res = search(maps)
#     return min(res) if res else -1
# def search(maps):
#     width, height = (len(maps[0]), len(maps))
#     stk = [((0, 0), 1, ((0, 0),))]
#     rec = set()
#     while stk:
#         curr = stk.pop()
#         if curr[0] == (height - 1, width - 1): 
#             rec.add(curr[1])
#             continue
#         for dir in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
#             x_check, y_check = (curr[0][0] + dir[0], curr[0][1] + dir[1])
#             if x_check < 0 or y_check < 0 or x_check > height - 1 or y_check > width - 1: continue
#             if maps[x_check][y_check] == 0: continue
#             if (x_check, y_check) in curr[2]: continue
#             stk.append(((x_check, y_check), curr[1] + 1, curr[2] + ((x_check, y_check),)))
#     return rec
### The code above proved to be a DFS. Here's the alleged BFS
from collections import deque
def solution(maps):
    return search(maps)
def search(maps):
    # init map size
    width, height = (len(maps[0]), len(maps))
    # init dir vectors
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # init starting point 0, 0
    dq = deque([((0, 0), 1)]) # x, y, path cnt
    # init paths record
    rec = set((0, 0))
    # loop
    while dq:
        # pop elem
        (x_curr, y_curr), cnt = dq.popleft()
        # curr == goal -> return
        if (x_curr, y_curr) == (height - 1, width - 1): # fixed goal
            return cnt
        # directions check relative to curr
        for dir in dirs:
            x_check, y_check = x_curr + dir[0], y_curr + dir[1]
            # boundaries check + blockade check + dupe check AIO
            if 0 <= x_check < height and \
                0 <= y_check < width and \
                maps[x_check][y_check] == 1 and \
                (x_check, y_check) not in rec:
                    rec.add((x_check, y_check))
                    dq.append(((x_check, y_check), cnt + 1))
            # big diff from the prev code is, that we don't need to keep track of individual case's paths records because bfs fans out to every possible paths every step.
    # defaults to -1 if goal hasn't been reached
    return -1