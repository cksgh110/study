arr_a = [[-1]*15 for i in range(5)]
arr_b = []
for i in range(5) :
    word = list(input())
    len_word = len(word)
    for j in range (len_word):
        arr_a[i][j]=word[j]
for i in range(15) :
    for j in range(5) : 
        if arr_a[j][i] == -1:
            continue
        else:
            arr_b.append(arr_a[j][i])
print(*arr_b,sep ='')