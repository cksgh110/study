chess_list=list(map(int,input().split()))
chess_real=[1,1,2,2,2,8]
for i in range(6):
    print(chess_real[i]-chess_list[i], end=' ')