word = input("")

word_count=[]
check=[]
def max_alphabet(word) :
    global word_count, check
    word_count= list(set(word.upper()))
    for i in word_count:
        check.append(word.upper().count(i))
    if check.count(max(check))>=2:
        return "?"
    return word_count[check.index(max(check))]
print(max_alphabet(word))
