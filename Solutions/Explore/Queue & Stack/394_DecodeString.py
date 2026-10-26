s1 = "3[a]2[bc]"
s2 = "3[a2[c]]"
s3 = "2[abc]3[cd]ef"

def sol(s):
    stk = []
    curr = 0
    ans = ""

    for ch in s:
        if ch.isdigit():
            curr = curr * 10 + int(ch)
        elif ch == "[":
            stk.append((ans, curr))
            ans = ""
            curr = 0
        elif ch == "]":
            prev_str, repeat = stk.pop()
            ans = prev_str + ans * repeat
        else:
            ans += ch

    return ans

print(sol(s1))
print(sol(s2))
print(sol(s3))