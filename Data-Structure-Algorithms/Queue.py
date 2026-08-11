#Queue is a data structure that follows the First-In, First-Out (FIFO) principle
# meaning the first element added is the first one to be removed.
queue = []

# Adding elements to the queue
queue.append('e')
queue.append('f')
queue.append('g')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("Elements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))

print("Queue after removing elements")
print(queue)