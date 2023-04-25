a,b=map(int,input().split())
card=list(map(int,input().split()))
low_sum=[]
for i in range(a):
    for j in range(a):
        if i==j:
            continue
        for k in range(a):
            if j==k or i==k:
                continue
            if b >= (card[i]+card[j]+card[k]):
                low_sum.append(card[i]+card[j]+card[k])
print(int(max(low_sum)))