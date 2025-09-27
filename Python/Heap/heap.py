import math


class Heap:
    """
    Heap condition:
        1. should be a Min. heap or Max. heap
        2. should be a complete binary tree (i.e., if rep. in array then no places is empty)

    Operations in Heap: insert(element) and delete()

    insert(element): node is inserted from the left side of the last level
    delete(): only root node can be deleted
    """

    def __init__(self, is_min_heap: bool = True):
        self.size = 0
        self.arr = []
        self.is_min_heap = is_min_heap
        # if is_min_heap:
        #     self.comp = lambda a, b: True if a < b else False
        # else:
        #     self.comp = lambda a, b: True if a > b else False

    def comparison(self, parent_data=-1, element_data=-1):
        if self.is_min_heap:
            return parent_data < element_data
        else:
            return parent_data > element_data

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def parent(self, i):
        return math.floor((i - 1) / 2)

    def insert(self, element):
        self.arr.append(element)
        self.fix(len(self.arr) - 1)
        self.size += 1

    def fix(self, pos):
        if pos > 0:
            parent_index = self.parent(pos)

            a = self.arr[parent_index]
            b = self.arr[pos]
            # via this user only has to specify when instantiating heap class
            if not self.comparison(parent_data=a, element_data=b):
                # swap
                [self.arr[pos], self.arr[parent_index]] = [
                    self.arr[parent_index],
                    self.arr[pos],
                ]

                # checks and fix position if heap is violated
                self.fix(parent_index)

    def delete(self):
        if self.size > 0:
            # swap root with last element
            [self.arr[0], self.arr[-1]] = [self.arr[-1], self.arr[0]]

            # remove last element
            self.arr.pop(-1)
            self.size -= 1

            # checks and fix position if heap is violated
            self.bubble_down(0)

    # fix_delete
    def bubble_down(self, i):
        left_index = self.left_child(i)
        right_index = self.right_child(i)

        # 1. no right child
        if left_index < len(self.arr) and right_index >= len(self.arr):
            a = self.arr[i]
            b = self.arr[left_index]

            if not self.comparison(
                parent_data=self.arr[i], element_data=self.arr[left_index]
            ):
                [self.arr[i], self.arr[left_index]] = [
                    self.arr[left_index],
                    self.arr[i],
                ]
                self.bubble_down(left_index)

        # 2. when both child exists
        elif left_index < len(self.arr) and right_index < len(self.arr):
            # find smallest among two child values
            smallest_index = left_index
            if self.arr[left_index] > self.arr[right_index]:
                smallest_index = right_index

            # check and swap elements if heap is violated
            if not self.comparison(parent_data=self.arr[i], element_data=self.arr[i]):
                [self.arr[i], self.arr[smallest_index]] = [
                    self.arr[smallest_index],
                    self.arr[i],
                ]
                self.bubble_down(smallest_index)

        # 3. when node is leaf node => nothing to do

    def display(self):
        print(self.arr)


# object instantiation
heap = Heap(is_min_heap=True)

heap.insert(5)
heap.insert(4)
heap.insert(2)
heap.insert(1)
heap.insert(7)
heap.insert(9)
heap.insert(0)

heap.display()

heap.delete()
heap.display()

heap.delete()
heap.display()

heap.delete()
heap.display()
