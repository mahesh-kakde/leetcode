s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"
s5 = "([)]"

def sol(s):
    br = {')':'(', ']':'[', '}':'{'}
    stk = []

    for c in s:
        if c not in br:
            stk.append(c)
        else:
            if not stk:
                return False
            else:
                popped = stk.pop()
                if popped != br[c]:
                    return False

    return not stk

print(sol(s1))
print(sol(s2))
print(sol(s3))
print(sol(s4))
print(sol(s5))