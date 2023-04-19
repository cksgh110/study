a=int(input())
b=int(input())
sum=0
min=0
def primenumber(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        for i in range (2,x-1):
            if x % i == 0:
                return 0
    return 1

for i in range(a,b+1):
    if sum ==0:
        if primenumber(i)==1:
            min=i
    sum +=i*primenumber(i)
if sum==0:
    print(-1)
else:
    print(sum)
    print(min)