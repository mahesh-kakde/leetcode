nums1 = [5,-5,1]
nums2 = [10,-5,-100]
nums3 = [4,7]

def sol(nums):
    ans = 0
    arrays = [nums]
        
    for i in range(len(nums)):
            new = nums[:i] + nums[i+1:]
            arrays.append(new)

    return arrays

print(sol(nums1))
print(sol(nums2))
print(sol(nums3))