tokens1 = ["2","1","+","3","*"]
tokens2 = ["4","13","5","/","+"]
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

from math import ceil, floor
def sol(tokens):
    stk = []

    for t in tokens:
        if t in '+-/*':
            b, a = stk.pop(), stk.pop()

            if t == '+':
                stk.append(a+b)
            elif t == '-':
                stk.append(a-b)
            elif t == '*':
                stk.append(a*b)
            elif t == '/':
                div = a/b
                if div < 0:
                    stk.append(ceil(div))
                else:
                    stk.append(floor(div))
        else:
            stk.append(int(t))

    return stk[0]

print(sol(tokens1))
print(sol(tokens2))
print(sol(tokens3))