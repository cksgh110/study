import sys
n = int(sys.stdin.readline())
word_list=[]
for i in range(n):
    word_list.append(sys.stdin.readline().rstrip())
word_list = list(set(word_list))
word_list.sort()
word_list.sort(key=lambda x:len(x))
for i in word_list:
    print(i)

