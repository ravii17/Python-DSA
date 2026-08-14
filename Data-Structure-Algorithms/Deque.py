def insertRear(self, key):
    if self.size == self.capacity:
        print("Deque is full")
        return
    rear = (self.front + self.size) % self.capacity
    self.arr[rear] = key
    self.size += 1