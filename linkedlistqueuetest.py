class QueueEmptyError(Exception):
    pass

class Queue:
    class Node:
        def __init__(self, element):
            self.next = None
            self.value = element

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def enqueue(self, element):
        node = self.Node(element)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyError("Queue is empty, consider enqueueing elements..")
        node = self.head
        self.head = node.next
        self.size -= 1
        return node.value

    def __repr__(self):
        queue_as_str = "<Queue Browse:\n"
        node = self.head
        while node is not None:
            queue_as_str += str(node.value) + '->'
            node = node.next
        return queue_as_str[:-2] + "\n>"


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue)


