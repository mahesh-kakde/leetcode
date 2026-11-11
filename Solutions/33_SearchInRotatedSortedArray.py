nums1, target1 = [4,5,6,7,0,1,2], 0
nums2, target2 = [4,5,6,7,0,1,2], 3
nums3, target3 = [1], 0

def sol(nums, target):
    n = len(nums)
    l = 0
    r = n - 1

    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m

    min_i = l

    if min_i == 0:
        l, r = 0, n - 1
    elif target >= nums[0] and target <= nums[min_i-1]:
        l, r = 0, min_i - 1
    else:
        l, r = min_i, n - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1

print(sol(nums1, target1))
print(sol(nums2, target2))
print(sol(nums3, target3))