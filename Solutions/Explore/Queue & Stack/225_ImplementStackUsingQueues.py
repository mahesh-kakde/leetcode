def sol():
    queue = []

    def push(x):
        queue.append(x)

        for _ in range(len(queue) - 1):
            queue.append(queue.pop(0))

    def pop():
        if not queue:
            return -1
        return queue.pop(0)

    def top():
        if not queue:
            return -1
        return queue[0]

    def empty():
        return len(queue) == 0

    return push, pop, top, empty

push, pop, top, empty = sol()

output = [None]
output.append(push(1))
output.append(push(2))
output.append(top())
output.append(pop())
output.append(empty())

print(output)