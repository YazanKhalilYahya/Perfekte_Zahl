x = int(input("Geben Sie bitte eine Ganzzahl ein:"))
liste = []
summe = 0
for i in range(1, x):
    if x%i == 0:
        liste.append(i)
for j in liste:
    summe += j
if x == summe:
    print(x, "ist eine perfekte Zahl.")
else:
    print("{} ist keine perfekte Zahl".format(x))




