nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]

# O(n^2)
def sol(nums):
    ans = []

    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        ans.append(product)

    return ans

# O(n)
def sol(nums):
    l_mult = 1
    r_mult = 1
    l_arr = [0] * len(nums)
    r_arr = [0] * len(nums)

    for i in range(len(nums)):
        j = -i - 1
        l_arr[i] = l_mult
        r_arr[j] = r_mult
        l_mult *= nums[i]
        r_mult *= nums[j]

    return [l_arr[i] * r_arr[i] for i in range(len(nums))]

print(sol(nums1))
print(sol(nums2))