from Linked_List.fundamentals.linked_list_program import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.ll = LinkedList()

    def top(self):
        if self.size > 0:
            return self.ll.head.data
        return None

    def push(self, value):
        self.ll.insert_at_front(value)
        self.size += 1

    def pop(self):
        self.ll.delete_at_front()
        self.size -= 1


st = Stack()

st.push(100)
st.push(300)
st.push(50)

print(f"Top element is = {st.top()}")

st.pop()

print(f"Top element is = {st.top()}")

st.pop()

print(f"Top element is = {st.top()}")
