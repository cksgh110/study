import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
n_list={}
m_list={}
answer=[]

for i in range(n):
    name = sys.stdin.readline().rstrip()
    n_list[name]=1
for i in range(m):
    name = sys.stdin.readline().rstrip()
    m_list[name]=1
for i in n_list:
    if i in m_list:
        answer.append(i)
    else:
        continue
answer.sort()
print(len(answer))
print(*answer,sep="\n")