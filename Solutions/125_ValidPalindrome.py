s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

def sol(s):
    new_s = ""

    for char in s:
        if char.isalnum():
            new_s += char.lower()

    return new_s == new_s[::-1]

print(sol(s1))
print(sol(s2))
print(sol(s3))