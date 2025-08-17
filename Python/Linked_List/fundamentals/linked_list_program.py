class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)

        # to add in a empty list
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_last(self, data):
        new_node = Node(data)

        # to add in a empty list
        if not self.head:
            self.insert_at_front(data)
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.next = None

    def insert_at_middle(self, data, position):
        new_node = Node(data)
        current_node = self.head

        if not self.head:
            print("Element cannot be inserted in the middle if the list is empty")
            return

        if position == 1:
            self.insert_at_front(data)
            return

        i = 2
        while i < position and current_node.next != None:
            current_node = current_node.next
            i += 1

        new_node.next = current_node.next
        current_node.next = new_node

    def delete_at_front(self):
        if not self.head:
            print("Nothing is there to delete!")
            return

        self.head = self.head.next

    def printList(self):
        if self.head == None:
            print("No element in the list")
            return

        current_node = self.head
        while current_node != None:
            print(f"{current_node.data} -> ", end="")
            current_node = current_node.next


my_list = LinkedList()

# my_list.insert_at_front(2)
# my_list.insert_at_front(4)
# my_list.insert_at_last(8)
# my_list.insert_at_last(1000)

# my_list.insert_at_middle(500, 1)

# my_list.printList()
