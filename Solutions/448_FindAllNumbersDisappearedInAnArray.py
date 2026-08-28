case1 = [4,3,2,7,8,2,3,1]
case2 = [1,1]

# time limit exceeded (O(n^2))
def sol(nums):
    comp = []

    for i in range(1, len(nums) + 1):
        comp.append(i)

    ans = []

    for num in comp:
        if num not in nums:
            ans.append(num)

    return ans

# 2 (accepted)
def sol(nums):
    comp = []

    for i in range(1, len(nums) + 1):
        comp.append(i)

    nums_set = set(nums)

    ans = []

    for num in comp:
        if num not in nums_set:
            ans.append(num)

    return ans

print(sol(case1))
print(sol(case2))