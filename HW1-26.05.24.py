def nod(a, b):
     if b == 0:
        return a
     else:
        return nod(b, a % b)
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
NOD = nod(a, b)
print(NOD)

