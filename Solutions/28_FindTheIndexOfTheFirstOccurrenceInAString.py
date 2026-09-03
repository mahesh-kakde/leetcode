# case 1
haystack1, needle1 = "sadbutsad", "sad"
# case 2
haystack2, needle2 = "leetcode", "leeto"

def sol(haystack, needle):
    for i in range(len(haystack)):
        j = 0
        while j < len(needle):
            if i + j >= len(haystack):
                break
            if haystack[i + j] != needle[j]:
                break
            j += 1

        if j == len(needle):
            return i

    return -1

print(sol(haystack1, needle1))
print(sol(haystack2, needle2))