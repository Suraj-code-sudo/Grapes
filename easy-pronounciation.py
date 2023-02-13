from tkinter.tix import Tree


string = "apple"
valid = False
alphas = [x for x in string]
if len(alphas) < 4:print("Yes")
for i in alphas[:5]:
    if i in ['a', 'e', 'i', 'o', 'u']:
        valid = True
        if valid is True:
            break

else:
    print("Yes")
