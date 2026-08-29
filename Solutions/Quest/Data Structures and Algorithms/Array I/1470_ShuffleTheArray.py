# case 1
nums1, n1 = [2,5,1,3,4,7], 3
# case 2
nums2, n2 = [1,2,3,4,4,3,2,1], 4

# 1
def sol(nums, n):
    a = nums[:n]
    b = nums[n:]
    ans = []

    for i in range(0, n):
        ans.append(a[i])
        ans.append(b[i])

    return ans

# 2
def sol(nums, n):
        ans = []
        
        for i in range(0, n):
            ans.append(nums[i])
            ans.append(nums[n+i])

        return ans

print(sol(nums1, n1))
print(sol(nums2, n2))