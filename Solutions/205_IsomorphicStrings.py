s1, t1 = "egg", "add"
s2, t2 = "f11", "b23"
s3, t3 = "paper", "title"

def sol(s, t):
    map1 = {}
    map2 = {}

    for i in range(len(s)):
        a = s[i]
        b = t[i]

        if a in map1 and map1[a] != b:
            return False

        if b in map2 and map2[b] != a:
            return False

        map1[a] = b
        map2[b] = a

    return True

print(sol(s1, t1))
print(sol(s2, t2))
print(sol(s3, t3))