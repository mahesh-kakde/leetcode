case1 = [-4,-2,1,4,8]
case2 = [2,-1,1]

def solution(nums):
    closest = nums[0]
    for x in nums:
        if abs(x) < abs(closest):
            closest = x

    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest

print(solution(case1))
print(solution(case2))