string = input()
result = string[0]
for i in string[1:len(string)]:
    result = result + ','+ i
print(result)
