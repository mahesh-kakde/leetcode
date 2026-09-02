case1 = [2,3]
case2 = [4,6]

# the new array can always be created:
# - if all odd/even - true
# - if some odd, and some even, we can always use the 2nd operation to create an odd, so True
def sol(nums):
    return True

print(sol(case1))
print(sol(case2))