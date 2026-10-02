n1 = 12
n2 = 13

from math import sqrt
def sol(n):
    ans = [n] * (n + 1)
    ans[0] = 0

    for i in range(1, n + 1):
        j = 1

        while j * j <= i:
            square = j * j
            ans[i] = min(ans[i], ans[i - square] + 1)
            j += 1

    return ans[n]

print(sol(n1)) # 3
print(sol(n2)) # 2