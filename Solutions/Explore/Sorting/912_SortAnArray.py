nums1 = [5,2,3,1]
nums2 = [5,1,1,2,0,0]

def sol(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = sol(nums[:mid])
    right = sol(nums[mid:])

    ans = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1

    while i < len(left):
        ans.append(left[i])
        i += 1

    while j < len(right):
        ans.append(right[j])
        j += 1

    return ans

print(sol(nums1))
print(sol(nums2))