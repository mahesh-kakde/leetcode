# case 1
word1, word2 = "abc", "pqr"
# case 2
word3, word4 = "ab", "pqrs"
# case 3
word5, word6 = "abcd", "pq"

def sol(arr1, arr2):
    ans = []

    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            ans.append(arr1[i])
            ans.append(arr2[i])

    elif len(arr1) < len(arr2):
        for i in range(len(arr1)):
            ans.append(arr1[i])
            ans.append(arr2[i])
        ans.append(arr2[len(arr1):])

    else:
        for i in range(len(arr2)):
            ans.append(arr1[i])
            ans.append(arr2[i])
        ans.append(arr1[len(arr2):])

    return "".join(ans)

print(sol(word1, word2))
print(sol(word3, word4))
print(sol(word5, word6))