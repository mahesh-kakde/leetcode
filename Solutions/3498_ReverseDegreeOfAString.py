s1 = "abc"
s2 = "zaza"

def sol(s):
    ans = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(s)):
        value = 26 - alphabet.index(s[i])
        ans += value * (i + 1)

    return ans

print(sol(s1)) # 148
print(sol(s2)) # 160