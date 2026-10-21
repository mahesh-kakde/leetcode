nums1, target1 = [1,3,5,6], 5
nums2, target2 = [1,3,5,6], 2
nums3, target3 = [1,3,5,6], 7

def sol(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l+r) // 2

        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m

    if nums[m] < target:
        return m + 1
    else:
        return m

print(sol(nums1, target1))
print(sol(nums2, target2))
print(sol(nums3, target3))