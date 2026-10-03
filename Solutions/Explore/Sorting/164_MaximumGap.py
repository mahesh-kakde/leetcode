nums1 = [3,6,9,1]
nums2 = [10]

def sol(nums):
    if len(nums) < 2:
        return 0

    nums.sort()

    diff = 0

    for i in range(len(nums)-1):
        curr = nums[i+1] - nums[i]
        diff = max(curr, diff)

    return diff

print(sol(nums1))
print(sol(nums2))