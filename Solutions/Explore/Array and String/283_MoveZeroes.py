case1 = [0,1,0,3,12]
case2 = [0]

def sol(nums):
    ans = []

    for num in nums:
        ans.append(num)
    
    for num in ans:
        if num == 0:
            ans.remove(num)
            ans.append(num)

    nums[:] = ans

    return nums

print(sol(case1))
print(sol(case2))