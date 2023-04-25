a=int(input())
n=1
list_666=[]
for i in range(10000):
    while True:
        n=n+1
        if str(n).find('666') != -1:
            list_666.append(n)
            break
print(list_666[a-1])


