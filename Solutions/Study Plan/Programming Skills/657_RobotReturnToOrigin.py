moves1 = "UD"
moves2 = "LL"

from collections import Counter
def sol(moves):
    moves = Counter(moves)
    return moves['U'] == moves['D'] and moves['L'] == moves['R']

print(sol(moves1))
print(sol(moves2))