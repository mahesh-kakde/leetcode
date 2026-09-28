nums1_1, nums1_2 = [1,2,2,1], [2,2]
nums2_1, nums2_2 = [4,9,5], [9,4,9,8,4]

from collections import Counter
def sol(nums1, nums2):
    freq1 = Counter(nums1)
    freq2 = Counter(nums2)
    ans = []

    for num in freq1:
        if num in freq2:
            for _ in range(min(freq1[num], freq2[num])):
                ans.append(num)

    return ans

print(sol(nums1_1, nums1_2))
print(sol(nums2_1, nums2_2))