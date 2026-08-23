case1 = [1, 2, 2, 4]
case2 = [1, 1]

def sol(nums):
    seen = set()

    for num in nums:
        if num in seen:
            duplicate = num
        seen.add(num)

    for num in range(1, len(nums) + 1):
        if num not in seen:
            missing = num
            break

    return [duplicate, missing]

print(sol(case1))
print(sol(case2))