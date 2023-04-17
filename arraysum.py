import numpy as np

N,M = map (int,input().split())
arr_1 = np.array([list(map(int, input().split())) for i in range(N)])
arr_2 = np.array([list(map(int, input().split())) for i in range(N)])
arr_sum = arr_1+arr_2
for i in range(N):
    print (*arr_sum[i])
