import numpy as np
string = "mononom"
word = 'mon'
str_letters = set(string)
str_words = set(word)
count_letters = [string.count(i) for i in str_letters]
count_words = [word.count(i) for i in str_words]
valid = 1
#print(count_words)
#print(count_letters)
inc = 0
zeros = [0]
diff = count_letters

def minus(differnce):
    differnce = [x - y for (x, y) in zip(differnce, count_words)]
    return differnce

result = minus(diff)
res = any(ele not in zeros for ele in result)
while res:
    result = minus(result)
    res = any(ele in zeros for ele in result)
    print(result)
