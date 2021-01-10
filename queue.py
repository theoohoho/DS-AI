""" Queue Implementation"""
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        del self.queue[0]
    def print_all(self):
        print(self.queue)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue('abc')
    queue.enqueue('def')
    queue.enqueue('qwe')
    queue.print_all()
    queue.dequeue()
    queue.print_all()
