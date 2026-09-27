nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

def sol(nums):
    if len(nums) != len(set(nums)):
        return True
    return False

print(sol(nums1))
print(sol(nums2))
print(sol(nums3))