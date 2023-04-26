import sys

word=str(sys.stdin.readline().rstrip())
word_dict={}
for i in range(len(word)):
    for j in range(i+1,len(word)+1):
        slicedword=word[i:j]
        if slicedword in word_dict:
            continue
        else:
            word_dict[slicedword]=1
print(len(word_dict))