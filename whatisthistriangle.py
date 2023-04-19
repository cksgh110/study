triangles = []
result = []
while True:
    triangle = input()
    if triangle == '0 0 0':
        break
    triangles.append(triangle)
for triangle in triangles:
    triangle = list(map(int,triangle.split()))
    if max(triangle)==min(triangle):
        print("Equilateral")
    elif not(triangle[0] + triangle[1] > triangle[2] and triangle[1] + triangle[2] > triangle[0] and triangle[2] + triangle[0] > triangle[1]):
        print("Invalid")
    elif triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[2] == triangle[0]:
        print("Isosceles")
    else:
        print("Scalene")