case1 = 3
case2 = 0
case3 = 1

def sol(index):
    ans = []

    for i in range(index + 1):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(ans[i - 1][j - 1] + ans[i - 1][j])
        ans.append(temp)

    return ans[index]

print(sol(case1))
print(sol(case2))
print(sol(case3))