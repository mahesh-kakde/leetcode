# case 1
nums1_1, m1, nums1_2, n1 = [1,2,3,0,0,0], 3, [2,5,6], 3
# case 2
nums2_1, m2, nums2_2, n2 = [1], 1, [], 0
# case 3
nums3_1, m3, nums3_2, n3 = [0], 0, [1], 1

def sol(nums1, m, nums2, n):
    ans = nums1[:m] + nums2
    ans.sort()
    nums1[:] = ans

print(sol(nums1_1, m1, nums1_2, n1))
print(sol(nums2_1, m2, nums2_2, n2))
print(sol(nums3_1, m3, nums3_2, n3))