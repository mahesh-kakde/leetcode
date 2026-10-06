nums1 = [2,1,2]
nums2 = [1,2,1,10]

# TLE
def sol(nums):
    ans = 0

    for i in range(len(nums) -2):
        for j in range(i + 1, len(nums) -1):
            for k in range(j + 1, len(nums)):
                if (nums[i] + nums[j]) > nums[k] and (nums[i] + nums[k]) > nums[j] and (nums[k] + nums[j]) > nums[i]:
                    curr = nums[i] + nums[j] + nums[k]
                    ans = max(ans, curr)

    return ans

# ACCEPTED
def sol(nums):
    nums.sort()
    ans = 0

    for i in range(len(nums) -2):
        if (nums[i] + nums[i + 1]) > nums[i + 2] and (nums[i] + nums[i + 2]) > nums[i + 1] and (nums[i + 2] + nums[i + 1]) > nums[i]:
            curr = nums[i] + nums[i + 1] + nums[i + 2]
            ans = max(ans, curr)

    return ans

print(sol(nums1))
print(sol(nums2))