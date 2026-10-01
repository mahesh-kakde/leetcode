deadends1, target1 = ["0201","0101","0102","1212","2002"], "0202"
deadends2, target2 = ["8888"], "0009"
deadends3, target3 = ["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"

from collections import deque
def sol(deadends, target):
    dead = set(deadends)

    if "0000" in dead:
        return -1

    queue = deque(["0000"])
    visited = {"0000"}
    steps = 0

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            if current == target:
                return steps

            for i in range(4):
                # forward
                next_combination = (current[:i]+str((int(current[i])+1) % 10)+current[i+1:])
                if next_combination not in dead and next_combination not in visited:
                    visited.add(next_combination)
                    queue.append(next_combination)
                # backwards
                next_combination = (current[:i]+str((int(current[i])-1) % 10)+current[i+1:])

                if next_combination not in dead and next_combination not in visited:
                    visited.add(next_combination)
                    queue.append(next_combination)

        steps += 1

    return -1

print(sol(deadends1, target1)) # 6
print(sol(deadends2, target2)) # 1
print(sol(deadends3, target3)) # -1