case1 = [1,0,2,3,0,4,5,0]
case2 = [1,2,3]
case3 = [1,0,2,3,0,4,5,0]

def sol(nums):
    ans = []

    for num in nums:
        if num == 0:
            ans.append(0)
            ans.append(0)
        else:
            ans.append(num)

        if len(ans) >= len(nums):
            break

    nums[:] = ans[:len(nums)]

print(sol(case1))
print(sol(case2))
print(sol(case3))