# case 1
s1, t1 = 'abcd', 'abcde'
# case 2
s2, t2 = '', 'y'
# case 3
s3, t3 = 'a', 'aa'

def sol(s, t):
    s = list(s)
    t = list(t)

    for ch in s:
        t.remove(ch)

    return t[0]

print(sol(s1, t1))
print(sol(s2, t2))
print(sol(s3, t3))