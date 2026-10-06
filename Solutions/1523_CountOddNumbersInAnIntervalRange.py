low1, high1 = 3, 7
low2, high2 = 8, 10

# MLE
def sol(low, high):
    ans = []

    if low % 2 != 0:
        for i in range(low, high+1, 2):
            ans.append(i)
    else:
        for i in range(low+1, high+1, 2):
            ans.append(i)

    return len(ans)

# ACCEPTED
def sol(low, high):
    return (high + 1) // 2 - low // 2

print(sol(low1, high1))
print(sol(low2, high2))