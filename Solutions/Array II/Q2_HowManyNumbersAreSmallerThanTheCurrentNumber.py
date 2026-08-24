case1 = [8,1,2,2,3]
case2 = [6,5,4,8]
case3 = [7,7,7,7]

def sol(nums):
    ans = []

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[j] < nums[i]:
                count += 1

        ans.append(count)

    return ans

print(sol(case1))
print(sol(case2))
print(sol(case3))