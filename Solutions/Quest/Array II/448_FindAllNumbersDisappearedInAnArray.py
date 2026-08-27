case1 = [4,3,2,7,8,2,3,1]
case2 = [1,1]

def sol(nums):
    seen = set()
    ans = []

    for num in nums:
        seen.add(num)

    for num in range(1, len(nums) + 1):
        if num not in seen:
            ans.append(num)

    return ans

print(sol(case1))
print(sol(case2))