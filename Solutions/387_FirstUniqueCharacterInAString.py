s1 = "leetcode"
s2 = "loveleetcode"
s3 = "aabb"

from collections import Counter
def sol(s):
    freq = Counter(s)

    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    return -1

print(sol(s1))
print(sol(s2))
print(sol(s3))