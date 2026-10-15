import csv
from pathlib import Path


filnavn = Path(__file__).with_name("sinnes_2014_2025_med_makstemperatur.csv")


def antall_varme_dager():
    valgt_år = input("Skriv inn et år: ").strip()
    sommerdager = 0
    hoysommerdager = 0
    tropedager = 0

    try:
        with filnavn.open("r", newline="", encoding="utf-8-sig") as fil:
            leser = csv.DictReader(fil, delimiter=";")

            for rad in leser:
                dato = (rad.get("Tid(norsk normaltid)") or "").strip()
                if not dato.endswith(valgt_år):
                    continue

                temperatur = (rad.get("Maksimumstemperatur (døgn)") or "").strip()
                if temperatur in ("", "-"):
                    continue

                temperatur = float(temperatur.replace(",", "."))

                if temperatur > 20:
                    sommerdager += 1
                if temperatur > 25:
                    hoysommerdager += 1
                if temperatur > 30:
                    tropedager += 1

        print("Antall sommerdager:", sommerdager)
        print("Antall hoysommerdager:", hoysommerdager)
        print("Antall tropedager:", tropedager)

    except FileNotFoundError:
        print("Filen ble ikke funnet:", filnavn)
    except ValueError:
        print("En temperatur i filen kunne ikke gjøres om til tall.")


antall_varme_dager()