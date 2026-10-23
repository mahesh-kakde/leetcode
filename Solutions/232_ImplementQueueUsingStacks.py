def sol():
    in_stack = []
    out_stack = []

    def push(val):
        in_stack.append(val)

    def pop():
        if not out_stack:
            while in_stack:
                out_stack.append(in_stack.pop())

        if not out_stack:
            return -1

        return out_stack.pop()

    def peek():
        if not out_stack:
            while in_stack:
                out_stack.append(in_stack.pop())

        if not out_stack:
            return -1

        return out_stack[-1]

    def empty():
        return not in_stack and not out_stack

    return push, pop, peek, empty

push, pop, peek, empty = sol()

output = [None]
output.append(push(1))
output.append(push(2))
output.append(peek())
output.append(pop())
output.append(empty())

print(output)