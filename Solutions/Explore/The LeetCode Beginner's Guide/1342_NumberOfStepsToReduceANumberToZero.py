case1 = 14
case2 = 8
case3 = 123

def sol(n):
    ans = 0

    while n != 0:
        if n%2 == 0:
            n = n/2
            ans += 1
        else:
            n = n-1
            ans += 1

    return ans

print(sol(case1))
print(sol(case2))
print(sol(case3))