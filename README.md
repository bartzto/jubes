# JuBeS
**Ju**ra **Be**zahl **S**ystem

*Ein Bezahlsystem mit RFID-Karten für eine Jura Kaffeemaschine.*

# Projektplanung
**Stakeholder:** Ausbilder

**Team:** Lukas Holzner, Tobias Bartz

## Zeitplan
**Bepsrechungstermin:** Donnerstag, 29.01.2020

## Grafische Darstellung
![Grafik](https://github.com/MeisterGig/jubes/blob/master/JuBeS-EPK.svg)

## Nicht Ziele
- Grafische Oberfläche zum Guthaben aufladen


## Risikoanalyse
| Problem | Lösung | Wahrscheinlichkeit |
|--- |--- |--- |
| Datenverlust | Backups | Mittel |
| Leute zahlen nicht | Zugriffsbeschränkungen | Hoch |
| Hacking | Hardware-Zugriff erschweren | Gering
| Stromausfall | -/- | Gering |

## Ressourcen

ESP32, Buzzer, I2C LCD Bildschirm, RFID Leser, Kabel


## Meilensteine
- [x] Karten erkennen **(1 Tag)**
- [ ] Karten IDs abspeichern **(1 Tag)**
- [ ] Buttons / Funktionen einbauen **(1 Tag)**
- [ ] Bildschirm **(1 Tag)**
- [ ] Bluetooth-Verbindung zum Karten aufladen **(1 Tag)**
- [ ] Physische Beschränkung an der Kaffeemaschine **( 1 1/2 Tage)**
- [x] Wartemusik mit Buzzer z.B.: Tetris **(2 Stunden)**
- [ ] Anbindung an die Jura Kaffeemaschine **(3 Tage)**


