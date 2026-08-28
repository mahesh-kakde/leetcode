case1 = [3,1,2,4]
case2 = [0]

def sol(nums):
    odd = []
    even = []

    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even + odd

print(sol(case1))
print(sol(case2))