#case 1
ransom1, magazine1 = "a", "b"
#case 2
ransom2, magazine2 = "aa", "ab"
#case 3
ransom3, magazine3 = "aa", "aab"

def sol(note, mag):
    mag = list(mag)

    for char in note:
        if char in mag:
            mag.remove(char)
        else:
            return False

    return True

print(sol(ransom1, magazine1))
print(sol(ransom2, magazine2))
print(sol(ransom3, magazine3))