case1 = [1,1,2]
case2 = [0,0,1,1,1,2,2,3,3,4]

def sol(nums):
    ans = []

    for i in nums:
        if i not in ans:
            ans.append(i)

    for i in range(len(ans)):
        nums[i] = ans[i]

    return len(ans)

print(sol(case1))
print(sol(case2))