a=int(input())
answer=[[0]*4 for i in range(a)]
for i in range(a):
    money=int(input())
    answer[i][0]=money//25
    money=money%25
    answer[i][1]=money//10
    money=money%10
    answer[i][2]=money//5
    answer[i][3]=money%5
for i in range(a):
    print(*answer[i])
