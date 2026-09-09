s1, t1 = "abc", "ahbgdc"
s2, t2 = "axc", "ahbgdc"
s3, t3 = "", "ahbgdc"

def sol(s, t):
    if s == "":
        return True
    
    j = 0
    for i in range(len(t)):
        if t[i] == s[j]:
            if j == len(s) - 1:
                return True
            j += 1
    return False

print(sol(s1, t1))
print(sol(s2, t2))
print(sol(s3, t3))