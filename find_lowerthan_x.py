a,b=map(int,input().split())
num_list=list(map(int,input().split()))
final_list=[]
for i in num_list:
    if i<b:
        final_list.append(i)
print(*final_list)
    