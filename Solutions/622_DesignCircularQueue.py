k1 = 3
k2 = 3

def sol(k):
    queue = [0] * k
    front = 0
    rear = 0
    size = 0

    def enQueue(value):
        nonlocal rear, size

        if size == k:
            return False

        queue[rear] = value
        rear = (rear + 1) % k
        size += 1

        return True

    def deQueue():
        nonlocal front, size

        if size == 0:
            return False

        front = (front + 1) % k
        size -= 1

        return True

    def Front():
        if size == 0:
            return -1
        return queue[front]

    def Rear():
        if size == 0:
            return -1

        index = (rear - 1 + k) % k
        return queue[index]

    def isEmpty():
        return size == 0

    def isFull():
        return size == k
    return enQueue, deQueue, Front, Rear, isEmpty, isFull

enQueue, deQueue, Front, Rear, isEmpty, isFull = sol(k1)

print(enQueue(1))
print(enQueue(2))
print(enQueue(3))
print(enQueue(4))
print(Rear())
print(isFull())
print(deQueue())
print(enQueue(4))
print(Rear())