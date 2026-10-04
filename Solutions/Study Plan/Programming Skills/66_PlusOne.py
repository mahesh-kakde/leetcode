case1 = [1,2,3]
case2 = [4,3,2,1]
case3 = [9]

def sol(nums):
    ans = []
    num_str = ''

    for num in nums:
        num_str = num_str + str(num)

    num_int = int(num_str) + 1
    num_str = str(num_int)

    for i in range(len(num_str)):
        ans.append(int(num_str[i]))

    return ans

print(sol(case1))
print(sol(case2))
print(sol(case3))