def sol():
    data = [[] for _ in range(1000)]

    def hash_func(key):
        return key % 1000

    def add(key):
        index = hash_func(key)
        if key not in data[index]:
            data[index].append(key)

    def remove(key):
        index = hash_func(key)
        if key in data[index]:
            data[index].remove(key)

    def contains(key):
        index = hash_func(key)
        return key in data[index]

    return add, remove, contains

add, remove, contains = sol()

add(1)
add(2)
print(contains(1))
print(contains(3))

remove(1)
print(contains(1))