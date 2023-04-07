def policzObwod(a):
    return 4*a

def policzPole(a):
    return a**2

expr = input("wpisz funkcję: ")

for a in range(12,23):
    if (expr=='policzObwod(a)'):
        print(f"Jeśli długość boku działki wynosi: {a} jej obwod wynosi {eval(expr)} m")
    elif (expr=='policzPole(a)'):
        print(f"Jeśli długość boku działki wynosi: {a} jej pole wynosi {eval(expr)} m2")
    else:
        print("taka funkcja nie istnieje")
        break

liczba = "6.7"

print(5*liczba)
print(5*eval(liczba))
