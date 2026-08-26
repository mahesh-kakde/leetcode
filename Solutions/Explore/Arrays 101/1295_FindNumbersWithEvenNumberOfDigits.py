case1 = [12,345,2,6,7896]
case2 = [555,901,482,1771]

def sol(nums):
    ans = 0

    for num in nums:
        if (len(str(num)) % 2) == 0:
            ans += 1

    return ans

print(sol(case1))
print(sol(case2))