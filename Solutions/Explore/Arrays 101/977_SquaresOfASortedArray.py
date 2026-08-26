case1 = [-4,-1,0,3,10]
case2 = [-7,-3,2,3,11]

def sol(nums):
    left = 0
    right = len(nums) - 1
    ans = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            ans.append(nums[left] ** 2)
            left += 1
        else:
            ans.append(nums[right] ** 2)
            right -= 1

    ans.reverse()
    return ans

print(sol(case1))
print(sol(case2))