case1 = [1,1,0,1,1,1]
case2 = [1,0,1,1,0,1]

def sol(nums):
    count = 0
    max_count = 0
    
    for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 0

    return max_count

print(sol(case1))
print(sol(case2))