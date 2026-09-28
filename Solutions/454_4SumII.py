nums1_1, nums1_2, nums1_3, nums1_4 = [1,2], [-2,-1], [-1,2], [0,2]
nums2_1, nums2_2, nums2_3, nums2_4 = [0], [0], [0], [0]
nums3_1, nums3_2, nums3_3, nums3_4 = [-1,-1], [-1,1], [-1,1], [1,-1]

# TLE
# def sol(nums1, nums2, nums3, nums4):
#     ans = 0
#     for i in range(len(nums1)):
#         for j in range(len(nums2)):
#             for k in range(len(nums3)):
#                 for l in range(len(nums4)):
#                     if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
#                         ans += 1

#     return ans

# HASH TABLE
from collections import Counter
def sol(nums1, nums2, nums3, nums4):
    sums = {}
    ans = 0

    for i in nums1:
        for j in nums2:
            sum1 = i + j
            if sum1 in sums:
                sums[sum1] += 1
            else:
                sums[sum1] = 1

    for k in nums3:
        for l in nums4:
            sum2 = -(k + l)
            if sum2 in sums:
                ans += sums[sum2]

    return ans

print(sol(nums1_1, nums1_2, nums1_3, nums1_4))
print(sol(nums2_1, nums2_2, nums2_3, nums2_4))
print(sol(nums3_1, nums3_2, nums3_3, nums3_4))