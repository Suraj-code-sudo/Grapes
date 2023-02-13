import math
n, m = map(int, input().split())
if n >= m:print(m)
else:
    q = math.ceil(m/n)
    m += q
    if m%n == 0:print(1)
    else:print(m%n)
    