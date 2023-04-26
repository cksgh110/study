import sys
n= sys.stdin.readline().rstrip()
n_dict={}
for i in map(int,sys.stdin.readline().rstrip().split()):
    if i in n_dict:
        n_dict[i]=int(n_dict[i])+1
    else:
        n_dict[i]=1
m= sys.stdin.readline().rstrip()
answer=[]
for i in map(int, sys.stdin.readline().rstrip().split()):
    if i in n_dict:
        answer.append(n_dict[i])
    else:
        answer.append(int(0))
print(*answer)