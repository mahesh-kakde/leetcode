case1 = [17,18,5,4,6,1]
case2 = [400]

def sol(nums):
    ans = []
    max_num = -1

    for i in range(len(nums) - 1, -1, -1):
        ans.append(max_num)

        if nums[i] > max_num:
            max_num = nums[i]

    ans.reverse()
    return ans

print(sol(case1))
print(sol(case2))