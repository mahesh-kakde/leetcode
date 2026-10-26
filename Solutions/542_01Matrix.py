mat1 = [[0, 0, 0],[0, 1, 0],[0, 0, 0]]
mat2 = [[0, 0, 0],[0, 1, 0],[1, 1, 1]]

from collections import deque
def sol(mat):
    m = len(mat)
    n = len(mat[0])
    q = deque()

    dist = [[-1] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                q.append((i, j))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < m and 0 <= nc < n
                    and dist[nr][nc] == -1):
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    return dist

print(sol(mat1))
print(sol(mat2))