nums1 = [3,4,5,1,2]
nums2 = [4,5,6,7,0,1,2]
nums3 = [11,13,15,17]

def sol(nums):
    n = len(nums)
    l = 0
    r = n - 1

    while l < r:
        m = (l + r) // 2

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m

    return nums[l]

print(sol(nums1))
print(sol(nums2))
print(sol(nums3))