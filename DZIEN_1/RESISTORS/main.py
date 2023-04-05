from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance

r1 = OldResistor(10.2E+2)
print(f"____ klasa: {r1.__class__.__name__} ____")
print(r1)
r1._ohms = 19
r1.set_ohms(1.4e+1)
print(r1.get_ohms())

r2 = Resistor(50.6E+3)
print(f"____ klasa: {r2.__class__.__name__} ____")
r2.ohms = 10.5e+2
print(f'układ elektryczny ma:\noporność: {r2.ohms} om\n'
      f'napięcie pradu: {r2.voltage} V\n'
      f'natężenie prądu: {r2.current} A\n')

r3 = VoltageResistance(1.1e+3)
print(f"____ klasa: {r3.__class__.__name__} ____")
print(f"natężenie początkowe prądu: {r3.current} A")
r3.voltage = 45
print(f"napięcie prądu: {r3.voltage} V")
print(f"natężenie  prądu: {r3.current} A")


r4 = BoundedResistance(1.7E+2)
print(f"____ klasa: {r4.__class__.__name__} ____")
try:
      r4.ohms = -2.7E+2
      print(f"oporność: {r4.ohms}")
except ValueError as v:
      print(v)

