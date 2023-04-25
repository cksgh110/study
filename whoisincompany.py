import sys
n = int(sys.stdin.readline())
new_log={}
for i in range(n):
    status = list(map(str,sys.stdin.readline().split()))
    if status[0] in new_log:
        del new_log[status[0]]
    new_log[status[0]]=status[1]
sorted_log = sorted(new_log.items(),reverse=True)
for name,status in sorted_log:
    if status=="enter":
        print(name)