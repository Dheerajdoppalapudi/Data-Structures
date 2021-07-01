class Dequeue:
    def __init__(self,limit):
        self.dequeue = []
        self.limit = limit

    def InsertionFront(self,data):
        if self.limit == len(self.dequeue):
            print('Queue is full ')
            return
        print('The data inserted at Front')
        self.dequeue.insert(0,data)

    def deletionFront(self):
        if len(self.dequeue) == 0:
            print('Queue is empty ')
        else:
            print("Poping element is Successfull")
            print(self.dequeue.pop(0))

    def InsertionLast(self,data):
        if len(self.dequeue) == self.limit:
            print('Queue is empty ')
            return
        print('The data that inserted at last ')
        self.dequeue.append(data)

    def deletionLast(self):
        if len(self.dequeue) == 0:
            print('queue is Empty ')
        else:
            print('Queue last element is deleted ',end = ' ')
            print(self.dequeue.pop())

    def GettingFront(self):
        if len(self.dequeue) == 0:
            print('queue is empty ')
        else:
            print(self.dequeue[0])

    def GettingLast(self):
        if len(self.dequeue) == 0:
            print('Queue is empty ')
        else:
            print(self.dequeue[-1])

    def isEmpty(self):
        if len(self.dequeue) == 0:
            print('Queue is Empty')
        else:
            print('Queue is not Empty')

    def isFull(self):
        if len(self.dequeue) == self.limit:
            print('Queue is Full')
        else:
            print('Queue is Not Full')

object = Dequeue(2)
while True:
    print('1 -> Insertion At front ')
    print('2 -> Insertion At Last ')
    print('3 -> deletion At Front ')
    print('4 -> deletion At Last ')
    print('5 -> Getting First element ')
    print('6 -> Getting last element ')
    print('7 -> is Empty or Not ')
    print('8 -> is Full or Not ')
    print('EXIT Press anything ')
    option=int(input('Enter the option '))
    if option == 1:
        data = int(input('Enter the data '))
        object.InsertionFront(data)
    elif option == 2:
        data = int(input('Enter the data '))
        object.InsertionLast(data)
    elif option == 3:
        object.deletionFront()
    elif option == 4:
        object.deletionLast()
    elif option == 5:
        object.GettingFront()
    elif option == 6:
        object.GettingLast()
    elif option == 7:
        object.GettingLast()
    elif option == 8:
        object.GettingLast()
    else:
        break