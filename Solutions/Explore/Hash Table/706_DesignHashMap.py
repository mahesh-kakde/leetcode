def sol():
    data = [[] for _ in range(1000)]

    def hash_func(key):
        return key % 1000

    def put(key, value):
        index = hash_func(key)
        for pair in data[index]:
            if pair[0] == key:
                pair[1] = value
                return
        data[index].append([key, value])

    def get(key):
        index = hash_func(key)
        for pair in data[index]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(key):
        index = hash_func(key)
        for i in range(len(data[index])):
            if data[index][i][0] == key:
                data[index].pop(i)
                return

    return put, get, remove

put, get, remove = sol()

put(1, 1)
put(2, 2)
print(get(1))
print(get(3))

put(2, 1)
print(get(2))

remove(2)
print(get(2))