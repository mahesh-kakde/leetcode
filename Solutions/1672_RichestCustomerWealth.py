case1 = [[1,2,3],[3,2,1]]
case2 = [[1,5],[7,3],[3,5]]
case3 = [[2,8,7],[7,1,3],[1,9,5]]

def sol(accounts):
    ans = 0

    for i in range(len(accounts)):
        curr = sum(accounts[i])
        if curr > ans:
            ans = curr

    return ans

print(sol(case1))
print(sol(case2))
print(sol(case3))