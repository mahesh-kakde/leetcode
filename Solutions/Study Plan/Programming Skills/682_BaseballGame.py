operations1 = ["5","2","C","D","+"]
operations2 = ["5","-2","4","C","D","9","+","+"]
operations3 = ["1","C"]

def sol(operations):
    ans = []

    for i in range(len(operations)):

        if operations[i] == "D":
            s = 2 * ans[-1]
            ans.append(s)
        elif operations[i] == "C":
            if len(ans) > 0:
                ans.pop()
        elif operations[i] == "+":
            s = ans[-1] + ans[-2]
            ans.append(s)
        else:
            ans.append(int(operations[i]))

    return sum(ans)

print(sol(operations1))
print(sol(operations2))
print(sol(operations3))