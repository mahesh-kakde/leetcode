case1 = ["h","e","l","l","o"]
case2 = ["H","a","n","n","a","h"]

# didnt modify the list in place
def sol(strs):
    ans = []

    for i in range(len(strs)-1, -1, -1):
        ans.append(strs[i])

    strs[:] = ans

# using two pointers
def sol(strs):
    left = 0
    right = len(strs) - 1

    while left < right:
        strs[left], strs[right] = strs[right], strs[left]

        left += 1
        right -= 1

print(sol(case1))
print(sol(case2))