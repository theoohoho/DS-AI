"""Linked list Implementation"""

class SingleListNode:
    def __init__(self, data):
        self.data = data
        self.pointer = None
        return


class SingleLinkedList:
    """
    Single linked list include following method:
    - insert: insert data
    - append: append data to last
    - remove:
    - search
    """

    def __init__(self):
        """ Initial linked list."""
        self.head = None
        self.tail = None
        return

    def print_all(self):
        curr_node = self.head
        while curr_node:
            print(f"Node data: {curr_node.data}")
            curr_node = curr_node.pointer

    def append(self, data):
        """ Add data into linked list."""
        node = SingleListNode(data)
        # if head is None means init node
        if not self.head:
            self.head, self.tail = (node, )*2
        else:
            self.tail.pointer = node
            self.tail = node
        return None

    def remove(self, data):
        # normal case:
        # deleted target is first node
        # deleted target is first node and have other data
        # deleted target inside list
        curr_node: SingleListNode = self.head
        while curr_node:
            next_node = curr_node.pointer
            if curr_node.data == data:
                if not next_node:
                    self.head, self.tail = None, None
                else:
                    self.head = next_node
                break
            elif next_node.data == data:
                curr_node.pointer = next_node.pointer
                break
            curr_node = next_node

    def search(self, target):
        """ Search target data that begin from head node."""
        next_node: SingleListNode = self.head
        while next_node:
            if next_node.data != target:
                next_node = next_node.pointer
                continue
            else:
                print(f'Find target: {next_node.data}')
                return next_node

    # def reverse(self):
    #     while True:
    # def insert_after(self, data, after_node):
    # def insert_before(self, data, before_node):


class DoubleListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.pointer = None
        return


if __name__ == '__main__':
    linked_list = SingleLinkedList()
    linked_list.append(123)
    linked_list.append('abc')
    linked_list.append(456)
    linked_list.print_all()
    linked_list.remove(456)
    linked_list.print_all()
    # linked_list.search('abc')
