case1 = [1,7,3,6,5,6]
case2 = [1,2,3]
case3 = [2,1,-1]

def sol(nums):
    ans = -1

    for i in range(len(nums)):
        sum_left = sum(nums[:i])
        sum_right = sum(nums[i+1:])

        if sum_left == sum_right:
            ans = i
            break

    return ans

print(sol(case1))
print(sol(case2))
print(sol(case3))