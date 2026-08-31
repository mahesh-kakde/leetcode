case1 = 5
case2 = 1

def sol(n):
    ans = []

    for i in range(n):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(ans[i - 1][j - 1] + ans[i - 1][j])
        ans.append(temp)

    return ans

print(sol(case1))
print(sol(case2))