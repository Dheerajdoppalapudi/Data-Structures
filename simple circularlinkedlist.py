class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertion(self, data): # adds a new node at the starting of the list
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

    def deletion(self): # deletes a node at starting of the list
        if self.head is None:
            print("List is empty, nothing to delete")
        else:
            temp = self.head
            while temp:
                if temp.next == self.head:
                    self.head = self.head.next
                    temp.next = self.head
                    return
                temp = temp.next

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


object=CircularLinkedList()
while True:
    print("----------------------------------")
    print('1 -> Insertion ')
    print('2 -> Traversal ')
    print('3 -> IsEmpty ')
    print('4 -> Deletion ')
    print('Press Any Key to Exit the Program')
    option = int(input('Enter the option '))
    if option == 1:
        data = int(input('Enter the data '))
        object.insertion(data)
    elif option == 2:
        object.showList()
    elif option == 3:
        object.isEmpty()
    elif option == 4:
        object.deletion()
    else:
        print('Program Terminated ')
        break