import math
AC=float(input("Длина первого  катета:"))
BC=float(input("Длина второго  катета:"))
AB=math.sqrt(AC**2 + BC**2)
P=AB+AC+BC
S=AC*BC/2
print("Площадь равна :",S,"Периметр равен:")
