word = input()
alphabet = list(range(97,123))

for a in alphabet:
    print(word.find(chr(a)))