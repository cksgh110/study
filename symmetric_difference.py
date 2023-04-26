import sys

a,b = map(int,sys.stdin.readline().rstrip().split())
list_a=list(map(int,sys.stdin.readline().rstrip().split()))
dict_a={string:i for i,string in enumerate(list_a)}
list_b=list(map(int,sys.stdin.readline().rstrip().split()))
dict_b={string:i for i,string in enumerate(list_b)}
dict_in={}
for i in dict_a:
    if i in dict_b:
        dict_in[i]=1
    else:
        continue
dict_a.update(dict_b)
count = int(len(dict_a)-len(dict_in))
print(count)