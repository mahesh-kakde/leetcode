case1 = [3,5,1]
case2 = [1,2,4]

def sol(nums):
    nums = sorted(nums)
    cd = abs(nums[0]-nums[1])
    for i in range(len(nums)-1):
        if abs(nums[i]-nums[i+1]) != cd:
            return False
    return True

print(sol(case1))
print(sol(case2))