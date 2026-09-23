text1 = "nlaebolko"
text2 = "loonbalxballpoon"
text3 = "leetcode"

def sol(text):
    freq = {}

    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return min(freq.get('b', 0), freq.get('a', 0), freq.get('l', 0)//2, freq.get('o', 0)//2, freq.get('n', 0))

print(sol(text1))
print(sol(text2))
print(sol(text3))