def average(array):
    length = len(set(array))
    a = sum(set(array))
    r = a / length
    return r

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)