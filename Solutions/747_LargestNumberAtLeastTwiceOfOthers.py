case1 = [3,6,1,0]
case2 = [1,2,3,4]
case3 = [0,0,0,1]

def sol(nums):
    largest = max(nums)

    for num in nums:
        if num != largest and largest < num * 2:
            return -1

    return nums.index(largest)

print(sol(case1))
print(sol(case2))
print(sol(case3))