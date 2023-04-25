N=int(input())
check_list=[]
for i in range(N):
    for j in range(N):
        if 3*i+5*j == N:
            check_list.append(int(i+j))
if check_list==[]:
    print(-1)
else:
    print(min(check_list))