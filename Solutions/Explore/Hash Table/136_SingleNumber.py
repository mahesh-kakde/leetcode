nums1 = [2,2,1]
nums2 = [4,1,2,1,2]
nums3 = [1]

def sol(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in nums:
        if freq[num] == 1:
            return num

print(sol(nums1))
print(sol(nums2))
print(sol(nums3))