a= int(input(""))
b= int(input(""))
total = 0
for i in range(0, b):
    price,c = map(int, input().split())
    total = total + price*c
if total ==a:
    print ("Yes")
else:
    print ("No")