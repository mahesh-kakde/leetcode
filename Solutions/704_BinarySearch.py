nums1, target1 = [-1,0,3,5,9,12], 9
nums2, target2 = [-1,0,3,5,9,12], 2

def sol(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(sol(nums1, target1))
print(sol(nums2, target2))