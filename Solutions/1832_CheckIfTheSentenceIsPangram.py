sentence1 = "thequickbrownfoxjumpsoverthelazydog"
sentence2 = "leetcode"

def sol(sentence):
    alpha = set("abcdefghijklmnopqrstuvwxyz")
    sentence = set(sentence)

    return alpha == sentence

# memory optimised
def sol(sentence):
    sentence = set(sentence)

    return len(sentence) == 26

print(sol(sentence1))
print(sol(sentence2))