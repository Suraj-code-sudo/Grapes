class Node:
   def __init__(self, data=None):
      self.val = data
      self.next = None

class Linked:
    def __init__(self):
        self.head = None
    
    def Insert(self):
        temp = self.head
        n = 0
        while(n>=0):
            n = int(input())
            n1 = Node(n)    
            temp.next = n1
            temp = temp.next

    def PrintList(self):
        printval = self.head
        while printval is not None:
            if printval.val == -1:
                break
            print(printval.val)
            printval = printval.next

l1 = Linked()
l1.Insert()
l1.PrintList()


# l1.head = Node(1)
# l1.head.next = Node(2)
# l1.head.next.next = Node(4)

# l2 = Linked()
# l2.head = Node(1)
# l2.head.next = Node(3)
# l2.head.next.next = Node(4)


# temp3 = Linked()
# temp1 = l1.head.next
# temp2 = l2.head.next
# temp3.head = l1.head if l1.head.val <= l2.head.val else l2.head
# result = temp3.head

# while(temp1 is not None):
#     print("Hello")
#     result.next = temp1 if temp1.val <= temp2.val else temp2
#     result = result.next
#     temp1 = temp1.next
#     temp2 = temp2.next

# print(result.val)
# #result.PrintList()
     