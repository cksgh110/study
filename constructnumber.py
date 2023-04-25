a=int(input())
numbers=[]
for i in range(a):
    x=i//100000+(i%100000)//10000+(i%10000)//1000+(i%1000)//100+(i%100)//10+i%10+i
    if x==a:
        numbers.append(i)
if numbers==[]:
    print(0)
else:
    print(int(min(numbers)))