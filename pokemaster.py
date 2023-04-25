import sys
n,m = map(int, sys.stdin.readline().split())
poke_list ={}
poke_list_2 = {}
answer =[]
for i in range(n):
    pokemon=sys.stdin.readline().rstrip()
    poke_list[i+1]=pokemon
poke_list_2 = {v:k for k,v in poke_list.items()}
for i in range(m):
    question=sys.stdin.readline().rstrip()
    if question.isnumeric() == True:
        answer.append(poke_list[int(question)])
    else:
        answer.append(poke_list_2.get(question))
for i in range(m):
    print(answer[i])