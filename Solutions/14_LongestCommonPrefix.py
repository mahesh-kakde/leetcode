case1 = ["flower","flow","flight"]
case2 = ["dog","racecar","car"]

def sol(strs):
    ans = strs[0]

    for s in strs[1:]:
        i = 0

        while i < len(ans) and i < len(s) and ans[i] == s[i]:
            i += 1

        ans = ans[:i]

    return ans

print(sol(case1))
print(sol(case2))