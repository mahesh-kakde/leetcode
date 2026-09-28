nums1, k1 = [1,1,1,2,2,3], 2
nums2, k2 = [1], 1
nums3, k3 = [1,2,1,2,1,2,3,1,3,2], 2

from collections import Counter
def sol(nums, k):
    nums = Counter(nums)
    ans = []

    for i in nums.most_common(k):
        ans.append(i[0])

    return ans

print(sol(nums1, k1))
print(sol(nums2, k2))
print(sol(nums3, k3))