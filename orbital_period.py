from math import pi
v=int(input("Орбитальная скорость(км/с)"))
r=int(input("Радиус орбиты(млн.км)"))
r*=1000000
t=2*pi*r/v
t=t/(60*24*60)
print(round(t))
