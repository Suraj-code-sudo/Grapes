s = "foo"
t = "bar"

def iso(s,t):
    for i in range(len(s)):
        if s.count(s[i]) != t.count(t[i]) or s[i] == t[i]:
            return False
    return True

res = iso(s,t)
print(res)

