nums1, target1 = [2,7,11,15], 9
nums2, target2 = [3,2,4], 6
nums3, target3 = [3,3], 6

def sol(nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(sol(nums1, target1))
print(sol(nums2, target2))
print(sol(nums3, target3))