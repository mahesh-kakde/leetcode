jewels1, stones1  = "aA", "aAAbbbb"
jewels2, stones2 = "z", "ZZ"

# O(len(jewels) * len(stones))
def sol(jewels, stones):
    ans = 0

    for jewel in jewels:
        for stone in stones:
            if jewel == stone:
                ans += 1

    return ans

# O(len(jewels) + len(stones))
from collections import Counter
def sol(jewels, stones):
    jewels = set(jewels)
    stones = Counter(stones)
    ans = 0

    for jewel in jewels:
        if jewel in stones:
            ans += stones[jewel]

    return ans

print(sol(jewels1, stones1))
print(sol(jewels2, stones2))