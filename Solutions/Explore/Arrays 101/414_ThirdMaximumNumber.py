case1 = [3,2,1]
case2 = [1,2]
case3 = [2,2,3,1]

def sol(nums):
    unique = sorted(set(nums))

    if len(unique) < 3:
        return max(unique)
    else:
        return unique[-3]

print(sol(case1))
print(sol(case2))
print(sol(case3))