jewels1, stones1  = "aA", "aAAbbbb"
jewels2, stones2 = "z", "ZZ"

def sol(jewels, stones):
    ans = 0

    for jewel in jewels:
        for stone in stones:
            if jewel == stone:
                ans += 1

    return ans

print(sol(jewels1, stones1))
print(sol(jewels2, stones2))