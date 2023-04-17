while True:
    try:
        a,b=map(int,input().split())
    except EOFError:
        break
    if a==b==0:
        break
    print(a+b)