import sys
n = int(sys.stdin.readline())
members=[]
for i in range(n):
    members.append(sys.stdin.readline().split())

members.sort(key=lambda x:int(x[0]))

for i in members:
    print(*i)