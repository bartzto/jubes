# JuBeS
**Ju**ra **Be**zahl **S**ystem

*Ein Bezahlsystem mit RFID-Karten für eine Jura Kaffeemaschine.*


#Installation

https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json Hinzufügen zu Preferences > Additional Board Manager URL

# Projektplanung
**Stakeholder:** Ausbilder

### Team
**Projektleiter:** Lukas Holzner

**Team Mitlgied:** Tobias Bartz

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
| Krankheit | Gesunde Ernährung | Hoch |

## Ressourcen

**Material:**
ESP32, Buzzer, I2C LCD Bildschirm, RFID Leser, Kabel, PCs

**Personal:**
Lukas Holzner, Tobias Bartz a 9 Tage

## Meilensteine
- [x] Karten erkennen **(1 Tag)**
- [ ] Karten IDs abspeichern **(1 Tag)**
- [ ] Buttons / Funktionen einbauen **(1 Tag)**
- [ ] Bildschirm **(1 Tag)**
- [ ] Bluetooth-Verbindung zum Karten aufladen **(1 Tag)**
- [ ] Physische Beschränkung an der Kaffeemaschine **( 1 1/2 Tage)**
- [x] Wartemusik mit Buzzer z.B.: Tetris **(2 Stunden)**
- [ ] Anbindung an die Jura Kaffeemaschine **(3 Tage)**


