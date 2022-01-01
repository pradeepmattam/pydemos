class StackEmptyError(Exception):
    pass


class Stack:
    class Node:
        def __init__(self, element):
            self.value = element
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, element):
        node = self.Node(element)
        if self.head is None:
            self.head = node
            node.next = None
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty, consider pushing some elements in..")
        node = self.head
        self.head = node.next
        node.next = None
        self.size -= 1
        return node.value

    def __repr__(self):
        stack_as_str = "<Stack with %s elements in it :\n" % self.size
        head = self.head
        while head is not None:
            stack_as_str += str(head.value) + "->"
            head = head.next
        stack_as_str += "\n>"
        return stack_as_str


stack = Stack()
print(stack)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
try:
    print(stack.pop())
except Exception as e:
    print(type(e))
    print(str(e))
