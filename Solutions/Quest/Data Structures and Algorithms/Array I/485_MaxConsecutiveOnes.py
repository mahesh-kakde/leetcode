case1 = [1,1,0,1,1,1]
case2 = [1,0,1,1,0,1]

def sol(nums):
    curr, ans = 0, 0

    for i in range(0, len(nums)):
        if nums[i] == 1:
            curr = curr + 1
            ans = max(curr, ans)
        else:
            curr = 0

    return ans

print(sol(case1))
print(sol(case2))