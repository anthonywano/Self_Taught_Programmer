class Stack:

    def __init__(self, l=[]):
        self.list = l
        self.l_size = len(self.list)

    def is_empty(self):
        if self.l_size == 0:
            return True
        else:
            return False

    def push(self, item):
        self.list.append(item)
        self.l_size += 1

    def pop(self):
        if self.l_size > 0:
            size = self.l_size-1
            item = self.list[size]

            self.list = self.list[:size]
            self.l_size -= 1

            return item

        else:
            return None

    def peek(self):
        if self.l_size > 0:
            size = self.l_size-1
            item = self.list[size]

            return item

        else:
            return None

    def size(self):
        return self.l_size




st = Stack('Yesterday')

reverse = ""
while not st.is_empty():
    reverse += st.pop()

print(reverse)
#print(''.join(reverse))






