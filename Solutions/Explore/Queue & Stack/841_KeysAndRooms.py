rooms1 = [[1],[2],[3],[]]
rooms2 = [[1,3],[3,0,1],[2],[0]]

from collections import deque
def sol(rooms):
    queue = deque([0])
    visited = {0}

    while queue:
        current = queue.popleft()

        for key in rooms[current]:
            if key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == len(rooms)

print(sol(rooms1))
print(sol(rooms2))