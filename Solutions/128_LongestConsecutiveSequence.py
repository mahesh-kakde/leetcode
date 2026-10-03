nums1 = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
nums3 = [1,0,1,2]

def sol(nums):
    sett = set(nums)
    ans = 0

    for num in sett:
        if num-1 not in sett:
            next_num = num+1
            curr = 1
            while next_num in sett:
                curr += 1
                next_num += 1
            ans = max(ans, curr)

    return ans

print(sol(nums1))
print(sol(nums2))
print(sol(nums3))