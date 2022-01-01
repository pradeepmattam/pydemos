class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def isempty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self):
        if self.isempty():
            raise ValueError("nothing to pop now!!")

        node = self.head
        self.head = self.head.next
        node.next = None
        self.size -= 1
        return node.value

    def display(self):
        node = self.head
        if self.isempty():
            print("Stack Empty")
        else:
            while node is not None:
                print(node.value, "->", end=" ")
                node = node.next
            return


stack = Stack()
stack.push("P")
stack.push("R")
stack.push("A")
stack.display()

print()
print("popping now ...")
stack.pop()
stack.pop()
stack.display()
print()
stack.pop()
stack.display()
print("no more stack entries after this..next pop() should raise error")
stack.pop()




