def sol():
    stack = []
    min_stack = []

    def push(val):
        stack.append(val)

        if not min_stack or val <= min_stack[-1]:
            min_stack.append(val)

    def pop():
        if not stack:
            return

        val = stack.pop()

        if val == min_stack[-1]:
            min_stack.pop()

    def top():
        if not stack:
            return -1
        return stack[-1]

    def getMin():
        if not min_stack:
            return -1
        return min_stack[-1]

    return push, pop, top, getMin

push, pop, top, getMin = sol()

output = [None]
output.append(push(-2))
output.append(push(0))
output.append(push(-3))
output.append(getMin())
output.append(pop())
output.append(top())
output.append(getMin())

print(output)