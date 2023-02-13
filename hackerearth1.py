inte = int(input())
num_lis = map(int, input().split())
ans = []

for num in num_lis:
    palindrome = 0
    for elem in range(num, 0, -1):
        binary = bin(elem)
        binary = binary[2:]

        if str(elem) == str(elem)[::-1] and binary == binary[::-1]:
            palindrome+=1
    
    ans.append(palindrome)
print(*ans)