import random

def sol():
    data = []
    index = {}

    def insert(val):
        if val in index:
            return False
        index[val] = len(data)
        data.append(val)
        return True

    def remove(val):
        if val not in index:
            return False
        i = index[val]
        last = data[-1]
        data[i] = last
        index[last] = i
        data.pop()
        del index[val]
        return True

    def get_random():
        return random.choice(data)
    return insert, remove, get_random

insert, remove, get_random = sol()

print(insert(1))
print(insert(2))
print(insert(2))

print(get_random())

print(remove(1))
print(remove(3))

print(get_random())