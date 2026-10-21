temperatures1 = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]
temperatures3 = [30,60,90]

def sol(temperatures):
    ans = [0] * len(temperatures)
    stk = []

    for i, t in enumerate(temperatures):
        while stk and stk[-1][0] < t:
            stk_t, stk_i = stk.pop()
            ans[stk_i] = i - stk_i

        stk.append((t, i))

    return ans

print(sol(temperatures1))
print(sol(temperatures2))
print(sol(temperatures3))