nums1, k1 = [1,2,3,1], 3
nums2, k2 = [1,0,1,1], 1
nums3, k3 = [1,2,3,1,2,3], 2

# TLE
def sol(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and abs(i-j) <= k:
                return True
    return False

# ACCEPTED
def sol(nums, k):
    seen = {}

    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i

    return False

print(sol(nums1, k1))
print(sol(nums2, k2))
print(sol(nums3, k3))