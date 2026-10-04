nums1 = [-1,-2,-3,-4,3,2,1]
nums2 = [1,5,0,2,-3]
nums3 = [-1,1,-1,1,-1]

def sol(nums):
    prod = 1

    for i in range(len(nums)):
        prod *= nums[i]

    def signFunc(x):
        if prod > 0:
            return 1
        elif prod < 0:
            return -1
        return 0

    return signFunc(prod)

print(sol(nums1))
print(sol(nums2))
print(sol(nums3))