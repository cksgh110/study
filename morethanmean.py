c = int(input(""))
over_avg = []
for i in range(c):
    score_list=list(map(int,input().split()))
    n = score_list[0]
    avg = (sum(score_list)-n)/(len(score_list)-1)
    count=0
    for j in range(1,n+1):
        if score_list[j] > avg:
            count=count+1
    over_avg.append((count/n)*100)
for i in range(c):
    print(f"{over_avg[i]:.3f}%")
