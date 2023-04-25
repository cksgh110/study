import sys
result=[]
n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
dic1 = {numbers[i]:i for i in range(n)}
m = int(sys.stdin.readline())
find_numbers = list(map(int,sys.stdin.readline().split()))
dic2 = {find_numbers[i]:i for i in range(m)}
for i in dic2:
    if i in dic1:
        result.append(1)
    else:
        result.append(0)
print(*result)