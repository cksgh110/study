a,b = map(int,input().split())
temp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer =''
while a !=0:
    answer +=str(temp[a%b])
    a = a//b
print(answer[::-1])