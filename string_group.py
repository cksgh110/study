import sys
word_group=[]
word_check=[]
count=0
n,m= map(int,sys.stdin.readline().split())
for i in range(n):
    word = sys.stdin.readline()
    word_group.append(word)
for i in range(m):
    word = sys.stdin.readline()
    word_check.append(word)
dic_group = {word_group[i]:i for i in range(n)}
for i,word in enumerate(word_check):
    if word in dic_group:
        count +=1
print(count)