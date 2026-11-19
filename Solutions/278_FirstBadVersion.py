# case 1
n1, bad1 = 5, 4
# case 2
n2, bad2 = 1, 1

# isBadVersion function
bad = 0
def isBadVersion(version):
    return version >= bad

def sol(n):
    l = 1
    r = n

    while l < r:
        m = (l + r) // 2
        if isBadVersion(m):
            r = m
        else:
            l = m + 1

    return l

# case 1
bad = bad1
print(sol(n1))
# case 2
bad = bad2
print(sol(n2))