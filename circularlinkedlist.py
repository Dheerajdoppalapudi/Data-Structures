class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertionAtHead(self, data): # adds a new node at the starting of the list
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
        else:
            temp = self.head
            while temp:
                if temp.next == self.head:
                    newNode.next = self.head
                    temp.next = newNode
                    return
                temp = temp.next

    def insertionAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            newNode.next = self.head
            temp.next = newNode

    def deletionAtHead(self): # deletes a node at starting of the list
        if self.head is None:
            print("List is empty, nothing to delete")
        elif self.head is self.head.next: # when there is only one node left in the linked list
            self.head = None
        else:
            oldhead = self.head
            self.head = self.head.next
            temp = self.head
            while temp.next is not oldhead:
                temp = temp.next
            temp.next = self.head

    def deletionAtEnd(self):
        if self.head is None:
            print("List is empty, nothing to delete")
        elif self.head is self.head.next: # when there is only one node left in the linked list
            self.head = None
        else:
            temp = self.head
            prevNode = None
            while temp.next is not self.head:
                prevNode = temp
                temp = temp.next
            prevNode.next = self.head
            temp = None

    def isEmpty(self):
        if self.head is None:
            print("List is Empty")
        else:
            print("List is not Empty")

    def showList(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=' ')
                if temp.next == self.head:
                    break
                temp = temp.next

n = CircularLinkedList()
n.insertionAtHead(1)
n.insertionAtHead(2)
n.insertionAtHead(3)
n.insertionAtHead(4)
n.insertionAtHead(5)
n.showList()
print()
n.insertionAtEnd(9)
n.showList()
print()
n.deletionAtEnd()
n.showList()
print()
n.deletionAtEnd()
n.showList()

