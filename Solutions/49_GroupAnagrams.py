strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

# TLE
def sol(strs):
    ans = []

    for word in strs:
        found = False

        for group in ans:
            if sorted(word) == sorted(group[0]):
                group.append(word)
                found = True
                break

        if not found:
            ans.append([word])

    return ans

# Accepted
def sol(strs):
    groups = {}

    for word in strs:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())

print(sol(strs1)) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(sol(strs2)) # [[""]]
print(sol(strs3)) # [["a"]]