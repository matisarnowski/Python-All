#! /usr/bin/python3

import math

print('Punkt kratowy to punkt, którego współrzędne w układzie kartezjańskim są liczbami całkowitymi. \nDane jest koło o środku w początku układu współrzędnych i promieniu r. \nZnajdź wszystkie punkty kratowe leżącewewnątrz takiego koła.')

promien = float(input('Podaj promień koła dla, którego chcesz znaleźć liczbę punktów kratowych. Może to być dowolna liczba wymierna: '))

liczba_punktow = 0

r = int(promien) + 1

for i in range(1, r):
    for j in range(r):
        if math.sqrt(i**2 + j**2) < promien:
            liczba_punktow += 1

liczba_punktow = 4 * liczba_punktow + 1

promien = str(promien)
liczba_punktow = str(liczba_punktow)

print('Liczba punktow kratowych w kole o promieniu ' + promien + ' wynosi: ' + liczba_punktow)
