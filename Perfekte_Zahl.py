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







"""import sys
zahl = int(input())
mylist = []
for i in range(1, zahl):
    if zahl % i == 0:
        mylist.append(i)

total = sum(mylist)


if total == zahl:
    print(zahl, "ist eine perfekte Zahl.")
else:
    print(zahl, "ist keine perfekte Zahl.")
"""