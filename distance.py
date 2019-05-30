import os, requests
os.system('clear')

print('*'*70)
print('*  Aplikacja oblicza trasę, podróży oraz szacunkowy jej czas,        *')
print('*  korzystając z API openrouteservice  https://openrouteservice.org  *')
print('*  dane podajemy w konwencji:  Ulica Nr Budynku Miasto               *')
print('*'*70)
print()

key ='Tu wstaw swój klucz z api.openrouteservice.org / Paste your key from api.openrouteservice.org'
start = input('Podaj adres (skąd): ')
end = input('Podaj adres (dokąd): ')

url ='https://api.openrouteservice.org/geocode/search?'

s = requests.get(url+ 'api_key=' + key + '&text=' + start)
e = requests.get(url+ 'api_key=' + key + '&text=' + end)

x = s.json()
y = e.json()

x1 = x['features'][0]['geometry']['coordinates'][0]
x2 = x['features'][0]['geometry']['coordinates'][1]
y1 = y['features'][0]['geometry']['coordinates'][0]
y2 = y['features'][0]['geometry']['coordinates'][1]

url2 = f'https://api.openrouteservice.org/v2/directions/driving-car?api_key={key}&start={x1},{x2}&end={y1},{y2}'

d = requests.get(url2)
z = d.json()
z1 = float(z['features'][0]['properties']['segments'][0]['distance'])
z2 = float(z['features'][0]['properties']['segments'][0]['duration'])
distance = round(z1/1000 ,2)
duration = round(z2/60,0)
duration_h = round((z2/60)/60,2)
print(f'Odległość: {distance} km, przewidywany czas podróży samochodem: {duration} min / (około {duration_h} godziny)')
