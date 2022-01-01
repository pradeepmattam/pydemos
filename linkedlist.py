class LL:
    class Node:
        def __init__(self, element):
            self.value = element
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def add(self, element):
        node = self.Node(element)
        if self.size == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def delete(self, element):
        node = self.head
        if node is None:
            return
        elif node.value == element:
            self.head = self.head.next
            self.size -= 1
            return
        while node.next is not None:
            if node.next.value == element:
                node.next = node.next.next
                self.size -= 1
                return
            node = node.next

    def __repr__(self):
        ll_as_str = ""
        node = self.head
        while node is not None:
            ll_as_str += str(node.value) + "->"
            node = node.next
        return ll_as_str[:-2]


ll = LL()
ll.add(10)
ll.add(20)
ll.add(10)
ll.add(10)
ll.add(30)
ll.add(50)
ll.add(10)
ll.add(60)
print(ll)
ll.delete(20)
print(ll)
ll.delete(30)
print(ll)
ll.delete(50)
print(ll)
ll.delete(10)
ll.delete(10)
ll.delete(10)
ll.delete(100)
ll.delete(10)
print(ll)
ll.delete(60)
print(ll)
ll.delete(10)
print(ll)

