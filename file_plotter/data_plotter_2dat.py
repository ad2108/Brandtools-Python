# file sorter
import matplotlib.pyplot as plt

print("Abaqus txt plotter")
print("Name der Datei1:")
name1 = input()
print("Name der Datei2:")
name2 = input()
print("Titel:")
titel = input()
print("X-Achsen Beschriftung")
x_achse = input()
print("Y-Achsen Beschriftung")
y_achse = input()
print("Legende 1 Beschriftung")
p1 = input()
print("Legende 2 Beschriftung")
p2 = input()
print("Faktor für x:")
faktorx = float(input())
print("Faktor für y:")
faktory = float(input())



# read and presort
data1 = open(name1 , "r")
unsorted1 = []

count = 1
for line1 in data1:
    if count > 2:
        unsorted1.append(line1.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1


data2 = open(name2 , "r")
unsorted2 = []

count = 1
for line2 in data2:
    if count > 2:
        unsorted2.append(line2.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1

# x, y Zuweisung
x1 = []
x2 = []
y = []
z = []
for element1 in unsorted1:
    count = 1
    for value1 in element1:
        if value1 != "":
            if count % 2 == 1:
                x1.append(float(value1) * faktorx)
            elif count % 2 == 0:
                y.append(float(value1) * faktory)
            count += 1

for element2 in unsorted2:
    count = 1
    for value2 in element2:
        if value2 != "":
            if count % 2 == 1:
                x2.append(float(value2) * faktorx)
            elif count % 2 == 0:
                z.append(float(value2) * faktory)
            count += 1
        

#plot
plt.figure(dpi=1200)
plt.plot(x1, y, label=p1)
plt.plot(x2, z, label=p2)
plt.title(titel)
plt.xlabel(x_achse)
plt.ylabel(y_achse)
plt.legend()
plt.grid()
plt.savefig(f"{name1}.pdf")
