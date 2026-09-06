target1, nums1 = 7, [2,3,1,2,4,3]
target2, nums2 = 4, [1,4,4]
target3, nums3 = 11, [1,1,1,1,1,1,1,1]

def sol(target, nums):
    left = 0
    total = 0
    ans = len(nums) + 1

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            ans = min(ans, right - left + 1)
            total -= nums[left]
            left += 1

    if ans == len(nums) + 1:
        return 0

    return ans

print(sol(target1, nums1))
print(sol(target2, nums2))
print(sol(target3, nums3))