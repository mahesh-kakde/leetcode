case1 = [-4,-1,0,3,10]
case2 = [-7,-3,2,3,11]

# NOT ACCEPTED
def squaring(nums):
    sqr = []
    for num in nums:
        sqr.append(num ** 2)
    return sqr

def sorting(sqr):
    n = len(sqr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if sqr[j-1] > sqr[j]:
                sqr[j-1], sqr[j] = sqr[j], sqr[j-1]
    return sqr

print(sorting(squaring(case1)))
print(sorting(squaring(case2)))


# ACCEPTED (USING 2 POINTERS, AS THE ARRAY IS ALREADY SORTED)
def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    result = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1

    result.reverse()
    return result

print(sortedSquares(case1))
print(sortedSquares(case2))

# OPTIMAL
def sortedSquares(nums):
    ans = []

    for i in nums:
        ans.append(i * i)

    ans.sort()
    return ans

print(sortedSquares(case1))
print(sortedSquares(case2))