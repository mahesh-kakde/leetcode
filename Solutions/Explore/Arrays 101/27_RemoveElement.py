# case 1
nums1, val1 = [3,2,2,3], 3
# case 2
nums2, val2 = [0,1,2,2,3,0,4,2], 2

def sol(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k, nums

print(sol(nums1, val1))
print(sol(nums2, val2))