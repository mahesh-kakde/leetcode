s1, t1 = "anagram", "nagaram"
s2, t2 = "rat", "car"

def sol(s, t):
    s = sorted(s)
    t = sorted(t)

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

print(sol(s1, t1))
print(sol(s2, t2))