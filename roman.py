
values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

roman = "IX"
decimal = 0
i=0

def addon(a, b):
    if a == 'I':
        if b == 'V':
            dec = 4
        elif b == 'X':
            dec = 9

    elif a == 'X':
        if b == 'L':
            dec = 40
        elif b == 'C':
            dec = 90

    elif a == 'C':
        if b == 'D':
            dec = 400
        elif b == 'M':
            dec = 900
    return dec
        
while(i<len(roman)):
    print(roman[i])
    if roman[i] in ['I'] and roman[i+1] in ['V', 'X']:
        decimal += addon(roman[i], roman[i+1])
        i+=2
    
    elif roman[i] in ['X'] and roman[i+1] in ['L', 'C']:
        decimal += addon(roman[i], roman[i+1])
        i+=2
    
    elif roman[i] in ['C'] and roman[i+1] in ['D', 'M']:
        decimal += addon(roman[i], roman[i+1])
        i+=2

    else:
        decimal += values[roman[i]]
        i+=1
if roman[-1] in ['I', 'X', 'C']:
    decimal += values[roman[-1]]
print(decimal)