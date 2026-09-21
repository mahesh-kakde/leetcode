words1 = ["gin","zen","gig","msg"]
words2 = ["a"]

def sol(words):
    code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    ans = []

    for i in range(len(words)):
        morse = ""
        for j in range(len(words[i])):
            ascii_value = ord(words[i][j])
            val = ascii_value - 97
            morse += code[val]
        ans.append(morse)

    return len(set(ans))

print(sol(words1))
print(sol(words2))