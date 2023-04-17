N,M = map(int,input().split())
sokuli =list(range(1,N+1))
sokuli1 = []
for x in range(M):
    i,j,k = map(int,input().split())
    sokuli = sokuli[:i-1]+sokuli[k-1:j]+sokuli[i-1:k-1]+sokuli[j:]
print (*sokuli)