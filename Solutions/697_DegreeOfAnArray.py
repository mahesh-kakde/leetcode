nums1 = [1,2,2,3,1]
nums2 = [1,2,2,3,1,4,2]

def sol(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    maxi = max(freq.values())

    first = {}
    last = {}

    for i in range(len(nums)):
        if nums[i] not in first:
            first[nums[i]] = i
        last[nums[i]] = i

    ans = len(nums)

    for num in freq:
        if freq[num] == maxi:
            length = last[num] - first[num] + 1
            ans = min(ans, length)

    return ans

print(sol(nums1)) # 2
print(sol(nums2)) # 6