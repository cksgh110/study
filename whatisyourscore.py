total_credit = 0
total_score = 0

for i in range(20):
    subject, a, b = map(str,input().split())
    if b == "P":
        continue
    else:
        a= int(float(a))
        if b == "A+":
            b1 = 4.5
        if b == "A0":
            b1 = 4.0
        if b == "B+":
            b1 = 3.5
        if b == "B0":
            b1 = 3.0
        if b == "C+":
            b1 = 2.5
        if b == "C0":
            b1 = 2.0
        if b == "D+":
            b1 = 1.5
        if b == "D0":
            b1 = 1.0
        if b == "F":
            b1 = 0
        total_credit +=a
        total_score +=a*b1
avg = total_score/total_credit
print(avg)
