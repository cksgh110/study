N,M = map(int,input().split())
arr_1 = [list(map(int, input().split())) for i in range(N)]
arr_2 = [list(map(int, input().split())) for i in range(N)]
arr_sum =[[0]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        arr_sum[i][j]=arr_1[i][j]+arr_2[i][j]
    print(*arr_sum[i])
