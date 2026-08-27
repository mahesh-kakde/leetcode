case1 = [2,1]
case2 = [3,5,5]
case3 = [0,3,2,1]

def sol(nums):
    n = len(nums)

    if n < 3:
        return False

    i = 0
    while i < n - 1 and nums[i] < nums[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    while i < n - 1:
        if nums[i] <= nums[i + 1]:
            return False
        i += 1

    return True

print(sol(case1))
print(sol(case2))
print(sol(case3))