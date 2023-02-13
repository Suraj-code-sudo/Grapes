class node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Linkedlist:
    def __init__(self):
        self.root = None

    def check(self):
        temp = self.root
        temp_2 = temp.left
        temp_3 = temp.right
        if N == 2 and M == 1:
            temp = temp.left
            print(temp.data)
        elif N == 2 and M == 2:
            temp = temp.right
            print(temp.data)
        elif N == 3 and M == 1:
            temp_2 = temp_2.left
            print(temp_2.data)
        elif N == 3 and M == 2:
            temp_2 = temp_2.right
            print(temp_2.data)
        elif N == 3 and M == 3:
            temp_3 = temp_3.left
            print(temp_3.data)
        else:
            N == 3 and M == 4
            temp_3 = temp_3.right
            print(temp_3.data)

if __name__ == "__main__":
    N, M = map(int, input().split())
    list1 = Linkedlist()
    list1.root = node("A")
    left_s = node("A")
    right_s = node("O")
    left_t = node("A")
    right_t = node("O")
    left_t1 = node("O")
    right_t2 = node("A")
    list1.root.left = left_s
    left_s.left = left_t
    left_s.right = right_t
    list1.root.right = right_s
    right_s.left = left_t1
    right_s.right = right_t2
    list1.check()
