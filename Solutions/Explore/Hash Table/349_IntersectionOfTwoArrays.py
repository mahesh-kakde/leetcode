nums1_1, nums1_2 = [1,2,2,1], [2,2]
nums2_1, nums2_2 = [4,9,5], [9,4,9,8,4]

def sol(nums1, nums2):
    ans = set()

    for num in nums1:
        if num in nums2:
            ans.add(num)

    return list(ans)

print(sol(nums1_1, nums1_2))
print(sol(nums2_1, nums2_2))