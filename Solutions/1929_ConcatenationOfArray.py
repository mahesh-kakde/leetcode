case1 = [1,2,1]
case2 = [1,3,2,1]

# 1
def sol(nums):        
    ans = []
    for i in range(0, len(nums)):
            ans.append(nums[i])

    for i in range(0, len(nums)):
            ans.append(nums[i])

    return ans

# 2
def sol(nums):        
    ans = []
    for i in range(0, len(nums)):
            ans.append(nums[i])

    return ans + ans

# 3
def sol(nums):        
    return nums + nums
    # unexpected

print(sol(case1))
print(sol(case2))