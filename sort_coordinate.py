import sys
n = int(sys.stdin.readline())
coordinate_list=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    coordinate_list.append([x,y])
coordinate_list.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    print(*coordinate_list[i])