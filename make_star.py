a=int(input(""))
for i in range(a):
    print(" "*(a-i-1)+"*"*(2*i+1))
for j in range(a-1):
    print(" "*(j+1)+"*"*(2*a-2*j-3))