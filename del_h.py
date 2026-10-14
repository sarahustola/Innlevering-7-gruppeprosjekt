import csv
from pathlib import Path


CSV_FIL = Path(__file__).with_name("sinnes_2014_2025_med_makstemperatur.csv")

with CSV_FIL.open(newline="", encoding="utf-8-sig") as fil:
    leser = csv.DictReader(fil, delimiter=";")
    rader = list(leser)

# Tell for det nyeste året som finnes i temperaturfilen. Hopp over tomme rader.
år = None
for rad in rader:
    dato = (rad.get("Tid(norsk normaltid)") or "").strip()
    if len(dato) >= 4 and dato[-4:].isdigit():
        rad_år = int(dato[-4:])
        if år is None or rad_år > år:
            år = rad_år

if år is None:
    raise ValueError("Fant ingen gyldige datoer i temperaturfilen.")

sommerdager = 0
høysommerdager = 0
tropedager = 0

for rad in rader:
    dato = (rad.get("Tid(norsk normaltid)") or "").strip()
    if not dato.endswith(str(år)):
        continue

    temperatur_verdi = (rad.get("Maksimumstemperatur (døgn)") or "").strip()
    temperatur = temperatur_verdi.replace(".", "").replace(",", ".")
    try:
        maks_temp = float(temperatur)
    except ValueError:
        continue

    if maks_temp > 20:
        sommerdager += 1
    if maks_temp > 25:
        høysommerdager += 1
    if maks_temp > 30:
        tropedager += 1

print(f"Antall sommerdager i {år}: {sommerdager}")
print(f"Antall høysommerdager i {år}: {høysommerdager}")
print(f"Antall tropedager i {år}: {tropedager}")
