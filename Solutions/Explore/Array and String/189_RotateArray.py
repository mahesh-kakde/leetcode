# case 1
nums1, k1 = [1,2,3,4,5,6,7], 3
# case 2
nums2, k2 = [-1,-100,3,99], 2

# time limit exceeded
def sol(nums, k):
    for i in range(k):
        last = nums.pop()
        nums.insert(0, last)

    return nums

# accepted
def sol(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

    return nums

print(sol(nums1, k1)) # [5,6,7,1,2,3,4]
print(sol(nums2, k2)) # [3,99,-1,-100]