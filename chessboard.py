n,m=map(int,input().split())
chess_board=[]
check_list=[]

for i in range(n):
    chess_board.append(input())
for i in range(n-7):
    for j in range(m-7):
        index1=0
        index2=0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2==0:
                    if chess_board[x][y] !='W':
                        index1 += 1
                    if chess_board[x][y] !='B':
                        index2 += 1
                else:
                    if chess_board[x][y] !='B':
                        index1 += 1
                    if chess_board[x][y] !='W':
                        index2 += 1
        check_list.append(min(index1,index2))
print(min(check_list))
            