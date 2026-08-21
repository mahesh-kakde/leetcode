case1 = "abcabcbb"
case2 = "bbbbb"
case3 = "pwwkew"

# NOT ACCEPTED
def longestSubstring(s):
    max_length = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]

            if len(set(substring)) == len(substring):
                max_length = max(max_length, len(substring))

    return max_length

print(longestSubstring(case1))
print(longestSubstring(case2))
print(longestSubstring(case3))


# ACCEPTED (USING A SET TO KEEP TRACK OF CHARACTERS)
def longestSubstring(s):
    max_length = 0

    for i in range(len(s)):
        seen = set()

        for j in range(i, len(s)):
            if s[j] in seen:
                break

            seen.add(s[j])
            max_length = max(max_length, j - i + 1)

    return max_length

print(longestSubstring(case1))
print(longestSubstring(case2))
print(longestSubstring(case3))

# OPTIMAL (USING SLIDING WINDOW)
def longestSubstring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

print(longestSubstring(case1))
print(longestSubstring(case2))
print(longestSubstring(case3))