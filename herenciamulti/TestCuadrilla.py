from herenciamulti.Persona import Persona as Perso
from herenciamulti.Supervisor import Supervisor

persona1 = Perso("V-50", "Leonardo", "Licon", "M")
persona2 = Perso("V-51", "Ankar", "Shidarta", "M")

print(persona1.nombre, persona1.apellido)

supervisor1 = Supervisor("V-16987456", "Jen", "Paz", "D", "Chivo")

print("The new worker is a:" + str(supervisor1))