class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def insertAtBeginning(last, key):
    newNode = Node(key)

    if last is None:
        newNode.next = newNode
        return newNode

    newNode.next = last.next
    last.next = newNode

    return last


def printList(last):
    if last is None:
        return

    head = last.next
    temp = head

    while True:
        print(temp.data, end="")
        temp = temp.next
        if temp != head:
            print(" -> ", end="")
        else:
            break
    print()


if __name__ == "__main__":
    # Create circular linked list: 2 -> 3 -> 4
    first = Node(2)
    first.next = Node(3)
    first.next.next = Node(4)

    last = first.next.next
    last.next = first

    # Insert 5 at the beginning
    last = insertAtBeginning(last, 5)

    printList(last)