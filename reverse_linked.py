class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def Print(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next


l1 = LinkedList()
l1.head = Node(1)
e2 = Node(2)
e2.next = Node(3)
l1.head.next = e2

temp2 = None
new = None
head = l1.head
while head:
    new = head.next
    head.next = temp2
    temp2 = head
    head = new


