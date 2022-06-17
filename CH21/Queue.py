class Queue:

    def __init__(self, l=[]):
        self.list = l

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        item = self.list[0]
        self.list = self.list[1:]

        return item

    def is_empty(self):
        return self.list == []

    def size(self):
        return len(self.list)


q1 = Queue()

for i in range(5):
    q1.enqueue(i)

print(q1.size())
print()

for i in range(5):
    print(q1.dequeue())

print()
print(q1.size())
