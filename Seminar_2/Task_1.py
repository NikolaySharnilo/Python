def sequence(n: int, mult: int) -> print:
    print(f"{n = }: ", end="")
    a = 1
    for i in range(1, n):
        a = a * mult
        print(f"{a} ", end=" ")


n = int(input("Введите число: "))
if n>0:
    sequence(n, -3)
    print()
else:
    print("Введите положительное число и повторите попытку")
