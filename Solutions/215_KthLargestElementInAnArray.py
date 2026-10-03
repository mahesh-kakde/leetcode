nums1, k1 = [3,2,1,5,6,4], 2
nums2, k2 = [3,2,3,1,2,4,5,5,6], 4

def sol(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]

print(sol(nums1, k1))
print(sol(nums2, k2))