class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linked:
    def __init__(self):
        self.head = None
    def prinb(self, head):
        rem = self.head
        while rem!=None:
            print(rem.data)
            rem = rem.next
def pushatfront(self, new_node):
    new_node = node(new_node)
    new_node.next,self.head = self.head,new_node

if __name__ == '__main__':
    for _ in range(5):
        l = linked()
        for _ in range(3):
            new_node = int(input())
            pushatfront(new_node)
    l.prinb()
        
    