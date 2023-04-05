from oldresistor import OldResistor
from resistor import Resistor

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
