nums1 = [1,2,3,4]
nums2 = [2,7,1,19,18,3]

def sol(nums):
    new = []
    n = len(nums)

    for i in range(1, n+1):
        if n % i == 0:
            new.append(nums[i-1]**2)

    return sum(new)

print(sol(nums1))
print(sol(nums2))