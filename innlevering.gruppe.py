import csv
import os

mappe = os.path.dirname(os.path.abspath(__file__))

filnavn = os.path.join(mappe, "sinnes_2014_2025.csv")

if not os.path.exists(filnavn):
    filnavn = os.path.join(
        mappe, "sinnes_2014_2025_med_makstemperatur.csv"
    )

lengde = 0
maks_lengde = 0
start = None
beste_start = None
beste_slutt = None

with open(filnavn, encoding="utf-8-sig", newline="") as fil:
    leser = csv.DictReader(fil, delimiter=";")

    for rad in leser:
        dato = rad["Tid(norsk normaltid)"].strip()
        nedbor = rad["Nedbør (døgn)"].strip().replace(",", ".")

        if nedbor == "" or nedbor == "-":
            lengde = 0
            start = None

        elif float(nedbor) == 0:
            if lengde == 0:
                start = dato

            lengde += 1

            if lengde > maks_lengde:
                maks_lengde = lengde
                beste_start = start
                beste_slutt = dato

        else:
            lengde = 0
            start = None

print("Lengste periode uten nedbør:", maks_lengde, "dager")
print("Startdato:", beste_start)
print("Sluttdato:", beste_slutt)