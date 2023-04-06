from pojazd import Pojazd

p1 = Pojazd()
lt = 56
odl = 620
cn = 6.81

print(f'splanie [litry/100 km]: {p1.spalanie100(odl,lt):.3f}')
print(f'koszty przejzdu na trasie {odl} km -> {p1.kosztprzejazdu(odl,lt,cn):.2f} zł')
