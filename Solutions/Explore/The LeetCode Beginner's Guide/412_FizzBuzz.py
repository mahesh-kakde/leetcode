case1 = 3
case2 = 5
case3 = 15

def sol(n):
    ans = []

    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            ans.append("FizzBuzz")
        elif i%3==0:
            ans.append("Fizz")
        elif i%5==0:
            ans.append("Buzz")
        else:
            ans.append(str(i))

    return ans

print(sol(case1))
print(sol(case2))
print(sol(case3))