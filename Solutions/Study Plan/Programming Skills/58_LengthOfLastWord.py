s1 = "Hello World"
s2 = "   fly me   to   the moon  "
s3 = "luffy is still joyboy"


def sol(s):
    s = s.split()
    return len(s[-1])

print(sol(s1))
print(sol(s2))
print(sol(s3))