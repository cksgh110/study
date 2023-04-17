arr= [list(map(int, input().split())) for i in range(9)]
max_arr = -1
for i in range(9):
    if max(arr[i])>max_arr:
        max_arr = max(arr[i])
        x = i+1
        y = arr[i].index(max_arr)+1
print(max_arr)
print(x,y)