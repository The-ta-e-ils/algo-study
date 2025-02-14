from collections import deque
from typing import List


def solution(maps: List[List[int]]) -> int:

	n = len(maps)
	m = len(maps[0])

	distance = [[-1] * m for _ in range(n)]
	moves = [[0, 1], [-1, 0], [0, -1], [1, 0]]

	def bfs(start):
		q = deque([start])
		distance[start[0]][start[1]] = 1

		while q:
			current_row, current_column = q.popleft()

			for step_row, step_column in moves:
				next_row, next_column = current_row + step_row, current_column + step_column

				if next_row < 0 or next_row >= n or next_column < 0 or next_column >= m:
					continue

				if maps[next_row][next_column] == 0:
					continue

				if distance[next_row][next_column] == -1:
					q.append([next_row, next_column])
					distance[next_row][next_column] = distance[current_row][current_column] + 1

	bfs([0, 0])

	return distance[n - 1][m - 1]
