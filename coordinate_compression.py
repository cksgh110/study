import sys
n = int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
num_sort=sorted(set(numbers))
dic={num_sort[i]:i for i in range(len(num_sort))}
for i in numbers:
    print(dic[i],end=' ')
