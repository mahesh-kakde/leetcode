case1 = "the sky is blue"
case2 = "  hello world  "
case3 = "a good   example"

def sol(strs):
    ans = ""

    words = strs.split()

    for i in range(len(words) - 1, -1, -1):
        ans += words[i]

        if i != 0:
            ans += " "

    return ans

print(sol(case1))
print(sol(case2))
print(sol(case3))