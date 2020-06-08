# Se pueden importar
# Modulos propios
# Modulos de terceros
# Modulos de Pythone

#import datetime
from datetime import timedelta, date

from mates.mikaMath import sumatoria, resta
from colorama import Fore, init

# Usando directamente import se llama como se ve abajo
#print(datetime.date.today())
print("La fecha actual es:", date.today())

#print(datetime.timedelta(minutes=70))
print("Formateo de:" + str(timedelta(minutes=70)))

init(convert=True)

print(Fore.RED + "***********************************")
print(Fore.GREEN + "El resultado de la sumatoria es:",sumatoria(30,20))
print(Fore.CYAN + "El resultado de la resta es:", resta(100,40))

print(Fore.RED + "************************************")
print(Fore.YELLOW + "Hello World Mikauran")