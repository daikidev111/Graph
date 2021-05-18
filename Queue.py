class Queue:
    def __init__(self):
        self.elements = []

    def append(self, data):
        self.elements.append(data)
        return data

    def pop(self):
        return self.elements.pop(0)

    #TODO fix the boundary problem later
    def rear(self):
        return self.elements[-1]

    def front(self):
        return self.elements[0]


if __name__ == '__main__':
    q = Queue()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)

    print(q.elements)
    print(q.front)

