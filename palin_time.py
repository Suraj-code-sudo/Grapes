a = "00:01"
k=0
hour, min = a.split(':')
print(min)
if hour == min[::-1]:
    print('0')
elif(hour == '00'):
    for j in range(1,70):
        if int(min)<10:
            print('->',k)
            k+=1
            min = (min[1]+str(k))
        elif int(min)>=10:
            min = str(int(min)+1)
        if int(min)%60 == 00:
                k=0
                hour = hour[1]+'1'
                min = '00'
        if str(hour) == str(min)[::-1]:
            print(min)
            break
    

# else:
#     min = int(min)
#     hour = int(hour)
#     for i in range(1,60):
#         min+=1
#         if hour%24 == 0:
#             min = 00
#             hour = 00
#         if min%60 == 0:
#             hour+=1
#         if str(hour) == str(min)[::-1]:
#             print(min)
#             break
