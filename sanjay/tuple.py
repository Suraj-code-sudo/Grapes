temp = []
for _ in range(5):
    temp.append(input())

tuple_ = (*temp, )

for string in range(len(tuple_)):
    print(string, tuple_[string])