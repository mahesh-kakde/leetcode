nums1 = [1,2,2,3]
nums2 = [6,5,4,4]
nums3 = [1,3,2]

def sol(nums):
    increasing = True
    decreasing = True

    for i in range(len(nums)-1):
        if nums[i + 1] > nums[i]:
            decreasing = False
        if nums[i + 1] < nums[i]:
            increasing = False

    return increasing or decreasing

print(sol(nums1))
print(sol(nums2))
print(sol(nums3))