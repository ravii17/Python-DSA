#Stack store data in LIFO manner 
stack = []

# append() function to push element in the stack
stack.append('e')
stack.append('f')
stack.append('g')

print('Initial stack')
print(stack)

# pop() function to pop element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())


print('\nStack after elements are popped:')
print(stack)