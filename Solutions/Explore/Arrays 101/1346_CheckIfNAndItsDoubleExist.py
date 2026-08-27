case1 = [10,2,5,3]
case2 = [3,1,7,11]
case3 = [0,0]

def sol(nums):

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == 2 * nums[j]:
                return True

    return False

print(sol(case1))
print(sol(case2))
print(sol(case3))