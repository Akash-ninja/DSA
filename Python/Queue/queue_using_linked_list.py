class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # insertion happens at the back
    def add(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # deletion happens at the front
    def remove(self):
        if self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.size -= 1
        else:
            print("No element to remove")

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.head.data:
            return self.head.data


q = Queue()
q.add(400)
q.add(200)
q.add(300)

while not q.isEmpty():
    print(f"Front element of queue is: {q.peek()}")
    q.remove()
