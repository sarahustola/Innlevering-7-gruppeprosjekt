

import matplotlib.pyplot as plt

filnavn = "Del 1/sinnes_2014_2025.csv"

årstall = input("Skriv inn et årstall: ")

datoer = []
snødybde = []
nedbør = []
temperatur = []
vind = []

plantevekst = 0
minimumsverdi = 5

with open(filnavn, "r", encoding="UTF-8") as fil:
    fil.readline()

    for linje in fil:
        kolonner = linje.strip().split(";")

        dato = kolonner[2]
        deler = dato.split(".")

        if len(deler) == 3:
            år = deler[2]
        else:
            continue

        if år == årstall:
            datoer.append(dato)

            if kolonner[6] != "-":
                snødybde.append(float(kolonner[6].replace(",", ".")))
            else:
                snødybde.append(None)

            if kolonner[4] != "-":
                nedbør.append(float(kolonner[4].replace(",", ".")))
            else:
                nedbør.append(None)

            if kolonner[3] != "-":
                temperatur.append(float(kolonner[3].replace(",", ".")))
            else:
                temperatur.append(None)

            if kolonner[5] != "-":
                vind.append(float(kolonner[5].replace(",", ".")))
            else:
                vind.append(None)

            if kolonner[3] != "-":
                temperatur_dag = float(kolonner[3].replace(",", "."))

                if temperatur_dag > minimumsverdi:
                    plantevekst += temperatur_dag - minimumsverdi

print("Total plantevekst i", årstall, ":", plantevekst)
plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plt.plot(datoer, snødybde)
plt.ylabel("Snødybde")
plt.title("Snødybde")

plt.subplot(4, 1, 2)
plt.plot(datoer, nedbør)
plt.ylabel("Nedbør")
plt.title("Nedbør")

plt.subplot(4, 1, 3)
plt.plot(datoer, temperatur)
plt.ylabel("Temperatur")
plt.title("Middeltemperatur")

plt.subplot(4, 1, 4)
plt.plot(datoer, vind)
plt.ylabel("Vind")
plt.title("Høyeste middelvind")

plt.xticks(rotation=45)
plt.xlabel("Dato")

plt.tight_layout()
plt.show()
