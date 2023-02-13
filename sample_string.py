text="ABCEF545"
lst=[x for x in range(1,10)]
#print(lst)
s=0
for x in range(0, len(text)):
    if text[x] in str(lst):
        print("==>",text[x])
        s=s+int(text[x])
        print(s)
        if text[x+1] not in str(lst) and not text[x+1]:break

print(s)