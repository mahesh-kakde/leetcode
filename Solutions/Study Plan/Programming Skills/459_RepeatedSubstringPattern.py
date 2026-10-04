s1 = "abab"
s2 = "aba"
s3 = "abcabcabcabc"

def sol(s):
    n = len(s)

    for i in range(1, n):
        if n % i == 0:
            curr = s[:i]
            if curr * (n // i) == s:
                return True

    return False

print(sol(s1))
print(sol(s2))
print(sol(s3))