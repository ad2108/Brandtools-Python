# file sorter
import matplotlib.pyplot as plt

print("Abaqus txt plotter")
print("Name der Datei:")
name = input()
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
print("Legende 3 Beschriftung")
p3 = input()
print("Umrechnungsfaktor für x:")
faktorx = float(input())
print("Umrechnungsfaktor für y")
faktory = float(input())
print("x minimal:")
xmin = float(input())
print("x maximal:")
xmax = float(input())
print("y minimal:")
ymin = float(input())
print("y minimal:")
ymax = float(input())



# read and presort
data = open(name , "r")
unsorted = []
count = 1
for line in data:
    if count > 2:
        unsorted.append(line.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1

# x, y Zuweisung
x = []
y = []
z = []
a = []
for element in unsorted:
    count = 1
    for value in element:
        if value != "":
            match count % 4:
                case 1:
                    x.append(float(value) * faktorx)
                case 2:
                    y.append(float(value) * faktory)
                case 3:
                    z.append(float(value) * faktory)
                case 0:
                    a.append(float(value) * faktory)
            count += 1
        

#plot
plt.figure(dpi=1200)
plt.axis([xmin, xmax, ymin, ymax])
plt.plot(x, y, label=p1)
plt.plot(x, z, label=p2)
plt.plot(x, a, label=p3)
plt.title(titel)
plt.xlabel(x_achse)
plt.ylabel(y_achse)
plt.legend()
plt.grid()
plt.savefig(f"{name}.pdf")
