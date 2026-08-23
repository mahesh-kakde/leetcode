# case 1
word1, word2 = "abc", "pqr"
# case 2
word3, word4 = "ab", "pqrs"
# case 3
word5, word6 = "abcd", "pq"

# ACCEPTED
def sol(arr1, arr2):
    solution = []

    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            solution.append(arr1[i])
            solution.append(arr2[i])

    elif len(arr1) < len(arr2):
        for i in range(len(arr1)):
            solution.append(arr1[i])
            solution.append(arr2[i])
        solution.append(arr2[len(arr1):])

    else:
        for i in range(len(arr2)):
            solution.append(arr1[i])
            solution.append(arr2[i])
        solution.append(arr1[len(arr2):])

    return "".join(solution)

print(sol(word1, word2))
print(sol(word3, word4))
print(sol(word5, word6))