a, b, c = map(int, input().split())
if a + b > c and b + c > a and a + c > b:
    print("Треугольник существует")
else:
    print("Нет")