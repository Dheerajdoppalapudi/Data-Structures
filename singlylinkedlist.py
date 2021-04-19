class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertionAtHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertionAtTail(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    def insertAtPos(self, data, pos):
        if self.head is None:
            print("Linked List is Empty")
        else:
            newNode = Node(data)
            lenlist = self.lengthOfList()
            if pos>lenlist+1:
                print("given position exceeds the max length of list")
            else:
                temp = self.head
                count = 1
                pos = pos - 1
                while temp:
                    if count == pos:
                        newNode.next = temp.next
                        temp.next = newNode
                        break
                    count += 1
                    temp = temp.next

    def insertionAfterKey(self, data, key):
        if self.head is None:
            print("Linked List is Empty")
        else:
            newNode = Node(data)
            temp = self.head
            while temp:
                if temp.data == key:
                    newNode.next = temp.next
                    temp.next = newNode
                    return
                temp = temp.next
            print("key not available")

    def insertAtKey(self, data, key):
        if self.head is None:
            print("Linked List is Empty")
        else:
            newNode = Node(data)
            temp = self.head
            prevNode = None
            while temp:
                if temp.data == key:
                    newNode.next = temp
                    prevNode.next = newNode
                    return
                prevNode = temp
                temp = temp.next
            print("Key not Available")

    def deletionAtHead(self):
        if self.head is None:
            print("List is empty nothing to delete")
        else:
            self.head = self.head.next

    def deletionAtTail(self):
        if self.head is None:
            print("List is empty nothing to delete")
        else:
            temp = self.head
            prevNode = None
            while temp.next:
                prevNode = temp
                temp = temp.next
            prevNode.next = None

    def deletionAtKey(self, key):
        if self.head is None:
            print("List is empty nothing to delete")
        else:
            temp = self.head
            prev = None
            while temp:
                if temp.data == key:
                    prev.next = temp.next
                    break
                prev = temp
                temp = temp.next
            print("key not Found to delete")

    def deletionAfterKey(self, key):
        if self.head is None:
            print("List is empty nothing to delete")
        else:
            temp = self.head
            prevNode = None
            while temp:
                if temp.data == key:
                    prevNode = temp
                    temp = temp.next
                    prevNode.next = temp.next
                    return
                prevNode = temp
                temp = temp.next
            print("key not Found to delete")

    def deletionAtPos(self, pos):
        if self.head is None:
            print("List is empty nothing to delete")
        else:
            lenList = self.lengthOfList()
            if pos>lenList+1:
                print("Position out of range to delete")
            else:
                temp = self.head
                prevNode = None
                count = 1
                while temp:
                    if count == pos:
                        prevNode.next = temp.next
                        return
                    count += 1
                    prevNode = temp
                    temp = temp.next

    def lengthOfList(self):
        if self.head is None:
            return 0
        else:
            temp = self.head
            count = 0
            while temp:
                count += 1
                temp = temp.next
            return count

    def showlist(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=' ')
                temp = temp.next

    def isempty(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            print("Linked List is not empty")

object = SinglyLinkedList()
while True:
    print("---------------------------------------")
    print("1 -> Print Linked list ")
    print("2 -> Insertion at head ")
    print("3 -> Insertion at tail ")
    print("4 -> Insertion at position ")
    print("5 -> Insertion after key ")
    print("6 -> Insertion at key ")
    print("7 -> Deletion at head ")
    print("8 -> Deletion at tail ")
    print("9 -> Deletion at key ")
    print("10 -> Deletion after key ")
    print("11 -> Deletion at position ")
    print("12 -> check if list is empty or not ")
    print("Enter any key to Exit program")
    option = int(input("Enter an Option : "))
    if option == 1:
        object.showlist()
    elif option == 2:
        data = int(input("enter the data: "))
        object.insertionAtHead(data)
    elif option == 3:
        data = int(input("enter the data: "))
        object.insertionAtTail(data)
    elif option == 4:
        data = int(input("enter the data: "))
        pos = int(input("enter the position: "))
        object.insertAtPos(data, pos)
    elif option == 5:
        data = int(input("enter the data: "))
        key = int(input("enter the key: "))
        object.insertionAfterKey(data, key)
    elif option == 6:
        data = int(input("enter the data: "))
        key = int(input("enter the key: "))
        object.insertAtKey(data, key)
    elif option == 7:
        object.deletionAtHead()
    elif option == 8:
        object.deletionAtTail()
    elif option == 9:
        key = int(input("enter the key: "))
        object.deletionAtKey(key)
    elif option == 10:
        key = int(input("enter the key: "))
        object.deletionAfterKey(key)
    elif option == 11:
        pos = int(input("enter the position: "))
        object.deletionAtPos(pos)
    elif option == 12:
        object.isempty()
    else:
        print("program Exited")
        break



