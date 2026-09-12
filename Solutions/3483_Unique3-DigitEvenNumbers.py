digits1 = [1,2,3,4]
digits2 = [0,2,2]
digits3 = [6,6,6]
digits4 = [1,3,5]

def sol(digits):
    ans = set()

    for i in range(len(digits)):
        for j in range(len(digits)):
            for k in range(len(digits)):

                if i==j or j==k or k==i:
                    continue

                if digits[i] == 0:
                    continue

                if digits[k] % 2 != 0:
                    continue

                num = digits[i]*100 + digits[j]*10 + digits[k]
                ans.add(num)
    return len(ans)

print(sol(digits1))
print(sol(digits2))
print(sol(digits3))
print(sol(digits4))