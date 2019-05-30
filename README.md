# distance
Aplikacja oblicza trasę, odległość i czas na podstawie api.openrouteservice.org w konsoli - funkcja w python-ie

# Przykład użycia

```
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python distance.py
```
wynik działania:

```
**********************************************************************
*  Aplikacja oblicza trasę, podróży oraz szacunkowy jej czas,        *
*  korzystając z API openrouteservice  https://openrouteservice.org  *
*  dane podajemy w konwencji:  Ulica Nr Budynku Miasto               *
**********************************************************************

Podaj adres (skąd): Warszawa Hoża 3
Podaj adres (dokąd): Szczecin Jasna 1
Odległość: 402.54 km, przewidywany czas podróży samochodem: 302.0 min / (około 5.04 godziny)
```
