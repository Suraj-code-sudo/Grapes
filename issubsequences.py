s ="twn"
t = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"

def subsequence(s, t):
    i = 0
    f = t.index(s[0])
    for c in range(f, len(t)):
        if s[i] == t[c]:
            i+=1
        if i == len(s):
            break
    return i == len(s)
print(subsequence(s,t))