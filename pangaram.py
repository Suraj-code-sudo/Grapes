A = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

total = ' '.join(A)
total = set(total)
total.remove(' ')

alphabets = 'abcdefghijklmnopqrstuvwxyz'
alphabets = set(alphabets)
if total == alphabets:
    print(1) 