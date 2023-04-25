import sys
n=int(sys.stdin.readline().rstrip())
card=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline().rstrip())
card_list={}
card_list_index=[0 for i in range(m)]
list_number=list(map(int,sys.stdin.readline().rstrip().split()))
for i, num in enumerate(list_number):
    card_list[num] = i
for i in card:
    if i not in card_list:
        continue
    a=card_list.get(i)
    card_list_index[a] +=1
print(*card_list_index)