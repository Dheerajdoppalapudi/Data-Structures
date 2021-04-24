class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertionAtHead(self, data):
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
                    self.head = newNode
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

    def insertionAtKey(self, data, key):
        if self.head is None:
            print("List is Empty")
        elif self.head.data == key:
            self.insertionAtHead(data)
        else:
            newNode = Node(data)
            temp = self.head
            prevNode = None
            while temp:
                if temp.data == key:
                    prevNode.next = newNode
                    newNode.next = temp
                    return
                if temp.next == key:
                    break
                prevNode = temp
                temp = temp.next
            print("Key Not Found")

    def deletionAtHead(self):
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

    def deletionAtKey(self, key):
        if self.head is None:
            print("Nothing to delete")
        elif self.head.data == key:
            self.deletionAtHead()
        else:
            temp = self.head
            prevNode = self.head
            while temp.next is not self.head:
                if temp.data == key:
                    prevNode.next = temp.next
                    return
                prevnode = temp
                temp = temp.next
            print("Key Not Found")

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

object = CircularLinkedList()
while True:
    print("----------------------------------")
    print('1 -> Insertion at Head ')
    print('2 -> Insertion at End ')
    print('3 -> Insertion at Key ')
    print('4 -> Deletion at head ')
    print('5 -> Deletion at End ')
    print('6 -> Deletion at Key ')
    print('7 -> Print List ')
    print('8 -> IsEmpty ')
    print('Press Any Key to Exit the Program')
    option = int(input('Enter the option '))
    if option == 1:
        data = int(input('Enter the data: '))
        object.insertionAtHead(data)
    elif option == 2:
        data = int(input('Enter the data: '))
        object.insertionAtEnd(data)
    elif option == 3:
        data = int(input('Enter the data: '))
        key = int(input("Enter the key: "))
        object.insertionAtKey(data, key)
    elif option == 4:
        object.deletionAtHead()
    elif option == 5:
        object.deletionAtEnd()
    elif option == 6:
        key = int(input("Enter the key: "))
        object.deletionAtKey(key)
    elif option == 7:
        object.showList()
    elif option == 8:
        object.isEmpty()
    else:
        print('Program Terminated ')
        print("For more function which perform different operation refer to singly linked linked list program.")
        print("As those un-included function also have same code for circular linked list i didn't add them here.")
        break
