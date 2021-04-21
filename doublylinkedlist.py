class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertionAtHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insertionAtLast(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp

    def insertionAtPosition(self, data, pos):
        if self.head is None:
            print("List is Empty")
        else:
            newNode = Node(data)
            temp = self.head
            prevNode = None
            count = 1
            while temp:
                if count == pos:
                    prevNode.next = newNode
                    newNode.prev = prevNode
                    temp.prev = newNode
                    newNode.next = temp
                    return
                count += 1
                prevNode = temp
                temp = temp.next
            print("position out of range")

    def insertionAtKey(self, data, key):
        if self.head is None:
            print("List is Empty")
        else:
            newNode = Node(data)
            temp = self.head
            prevNode = None
            while temp:
                if temp.data == key:
                    prevNode.next = newNode
                    newNode.prev = prevNode
                    newNode.next = temp
                    temp.prev = newNode
                    return
                prevNode = temp
                temp = temp.next
            print("key Not Found")

    def deletinAtHead(self):
        if self.head is None:
            print("nothing to delete")
        else:
            temp = self.head
            self.head = temp.next
            temp = None

    def deletionAtTail(self):
        if self.head is None:
            print("nothing to delete")
        else:
            temp = self.head
            prevNode = None
            while temp:
                if temp.next is None:
                    temp.prev = None
                    prevNode.next = None
                prevNode = temp
                temp = temp.next

    def deleteAtKey(self, key):
        if self.head is None:
            print("Nothing to Delete")
        else:
            temp = self.head
            prevNode = None
            nextNode = temp.next
            while temp:
                if temp.data == key:
                    prevNode.next = temp.next
                    nextNode.prev = temp.prev
                    temp = None
                    return
                prevNode = temp
                temp = temp.next
                nextNode = temp.next
            print("Key Not Found")

    def deletionAfterKey(self, key):
        if self.head is None:
            print("Nothing to Delete")
        else:
            temp = self.head
            nextNode = temp.next
            while temp:
                if temp.data == key:
                    if nextNode is None:
                        print("no next node to delete")
                        return
                    if nextNode.next is None:
                        temp.next = None
                        nextNode.prev = None
                        return
                    temp.next = nextNode.next
                    nextNode.next.prev = temp
                    break
                temp = temp.next
                nextNode = temp.next

    def deletionAtPos(self, pos):
        if self.head is None:
            print("Nothing to Delete")
        elif pos == 1:
            temp = self.head
            self.head = temp.next
            temp = None
        else:
            temp = self.head
            prevNode = None
            count = 1
            while temp:
                if count == pos:
                    if temp.next is None:
                        prevNode.next = None
                        return
                    prevNode.next = temp.next
                    temp.next.prev = prevNode
                    break
                count += 1
                prevNode = temp
                temp = temp.next

    def reverseTransversal(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            while temp:
                print(temp.data, end=' ')
                temp = temp.prev

    def isEmpty(self):
        if self.head is None:
            print("List is empty")
        else:
            print("List is not Empty")

    def showList(self):
        if self.head is None:
            print("linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=' ')
                temp = temp.next

object = DoublyLinkedList()
while True:
    print("---------------------------------------")
    print("1 -> print List ")
    print("2 -> insertion at Head ")
    print("3 -> insertion at Last")
    print("4 -> insertion at Position")
    print("5 -> insertion at Key")
    print("6 -> deletion at Head ")
    print("7 -> deletion at Tail ")
    print("8 -> deletion at Key ")
    print("9 -> deletion after Key ")
    print("10 -> deletion at position ")
    print("11 -> reverse Transversal ")
    print("12 -> check if list is empty or not ")
    option = int(input("Enter the option "))
    if option == 1:
        object.showList()
    elif option == 2:
        data = int(input("Enter the Data: "))
        object.insertionAtHead(data)
    elif option == 3:
        data = int(input("Enter the Data: "))
        object.insertionAtLast(data)
    elif option == 4:
        data = int(input("Enter the Data: "))
        pos = int(input("enter the position: "))
        object.insertionAtPosition(data, pos)
    elif option == 5:
        data = int(input("Enter the Data: "))
        key = int(input("enter the key: "))
        object.insertionAtKey(data, key)
    elif option == 6:
        object.deletinAtHead()
    elif option == 7:
        object.deletionAtTail()
    elif option == 8:
        key = int(input("enter the key: "))
        object.deleteAtKey(key)
    elif option == 9:
        key = int(input("enter the key: "))
        object.deletionAfterKey(key)
    elif option == 10:
        pos = int(input("enter the position: "))
        object.deletionAtPos(pos)
    elif option == 11:
        object.reverseTransversal()
    elif option == 12:
        object.isEmpty()
    else:
        print("program terminated")
        break