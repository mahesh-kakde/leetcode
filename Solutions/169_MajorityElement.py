nums1 = [3,2,3]
nums2 = [2,2,1,1,1,2,2]
nums3 = [6,5,5]

from collections import Counter
def sol(nums):
    n = len(nums)//2
    nums = Counter(nums)

    for keys, values in nums.items():
        if values > n:
            return keys
    return -1

def sol(nums):
    nums = Counter(nums)
    return max(nums, key=nums.get)

print(sol(nums1))
print(sol(nums2))
print(sol(nums3))