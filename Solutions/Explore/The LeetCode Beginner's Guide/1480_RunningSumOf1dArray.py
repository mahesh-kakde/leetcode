case1 = [1,2,3,4]
case2 = [1,1,1,1,1]
case3 = [3,1,2,10,1]

# 1
def sol(nums):
    ans = []

    for i in range(len(nums)):
        curr_sum = sum(nums[:i+1])
        ans.append(curr_sum)

    return ans

# 2
def sol(nums):
    ans = []
    curr_sum = 0

    for num in nums:
        curr_sum += num
        ans.append(curr_sum)

    return ans

print(sol(case1))
print(sol(case2))
print(sol(case3))