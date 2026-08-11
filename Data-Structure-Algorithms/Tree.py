class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

root = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")

root.children.append(node_b)
root.children.append(node_c)
node_b.children.append(node_d)
node_c.children.append(node_e)
print("Root:", root.data)

for child in root.children:
    print("Child:", child.data)

print("Child of B:", node_b.children[0].data)