n = 25

total = 0

def fact(n):
    i = 0
    j = 1
    for _ in range(n-1):
        k = j
        j = i+j
        i = k
    return j

total += fact(n-1)
total += fact(n-2)
total += fact(n-3)
print(total)
