nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]

# TLE
def sol(nums):
    ans = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    curr = []
                    curr.append(nums[i])
                    curr.append(nums[j])
                    curr.append(nums[k])
                    curr.sort()
                    if curr not in ans:
                        ans.append(curr)

    return ans

# ACCEPTED USING TWO POINTERS
def sol(nums):
    nums.sort()
    ans = []

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        low, high = i + 1, len(nums) - 1
        while low < high:
            summ = nums[i] + nums[low] + nums[high]
            if summ == 0:
                ans.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
            elif summ < 0:
                low += 1
            else:
                high -= 1

    return ans

print(sol(nums1))
print(sol(nums2))
print(sol(nums3))