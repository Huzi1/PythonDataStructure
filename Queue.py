#FIFO
class Queue:
    
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return self.stack == []

    def enqueue(self,data):

        return self.queue.append(data)  

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):

        return  self.queue[0]   