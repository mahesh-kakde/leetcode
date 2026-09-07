s1 = "Let's take LeetCode contest"
s2 = "Mr Ding"

def sol(s):
    ans = ""

    words = s.split()

    for i in range(len(words)):
        ans += words[i][::-1]

        if i != len(words) - 1:
            ans += " "

    return ans

print(sol(s1))
print(sol(s1))