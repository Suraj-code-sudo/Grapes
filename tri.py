A = '36'
B = '49'
fi = 0
for i in range(int(A), int(B)+1):
    res = 0
    for j in range(len(str(i))):
        res = res^int(str(i)[j]) 
    
    m = int(int(min(str(i)))+int(max(str(i))))/2
    print(res, m)
    if res > m:
        fi+=1
print(fi)