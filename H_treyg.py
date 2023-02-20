import math
a = int(input("Введите катет a: "))
b = int(input("Введите катет b: "))
c = math.sqrt(pow(a,2)+pow(b,2))
h = (a*b)/c
print ("Гипотенуза прямоугольного треугольника: ", h)