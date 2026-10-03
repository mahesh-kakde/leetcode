case1 = [1,1,4,2,1,3]
case2 = [5,1,2,3,4]
case3 = [1,2,3,4,5]

def sol(nums):
    ans = 0
    sorted_nums = sorted(nums)

    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            ans += 1

    return ans

print(sol(case1))
print(sol(case2))
print(sol(case3))