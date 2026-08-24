case1 = 'III'
case2 = 'LVIII'
case3 = 'MCMXCIV'

def sol(roman):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    ans = 0

    for i in range(len(roman)):
        if i + 1 < len(roman) and d[roman[i]] < d[roman[i + 1]]:
            ans -= d[roman[i]]
        else:
            ans += d[roman[i]]

    return ans

print(sol(case1)) # 3
print(sol(case2)) # 58
print(sol(case3)) # 1994