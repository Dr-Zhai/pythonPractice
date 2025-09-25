class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            print("节点不存在")
            return
        if prev:
            prev.next = current.next
        else:
            self.head = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            return False

ll = LinkedList()
ll.insert_at_tail(1)
ll.print_list()
ll.insert_at_tail(2)
ll.print_list()
ll.insert_at_head(0)
ll.print_list()
ll.delete_node(1)
ll.print_list()
