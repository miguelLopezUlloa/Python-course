class MiClase:
    varible_clase = "Variable de clase"
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
print(MiClase.varible_clase)

objeto1 = MiClase("Variable de Instancia cadena")

# Se asocia con la clase el valor nuevo. Antes no esta ligadoe
MiClase.varible_clase = "Modificando valor de Variable de Instancia"

print(MiClase.varible_clase) # Son valores distinto
print("El objeto1 tiene:", objeto1.variable_instancia) # Son valores distintos

#Podemos acceder a la las variable de clase desde el Objeto
print("El valor desde el objeto hacia el attributo es:",objeto1.varible_clase)

#Tambien se puede acceder al atributo desde la clase misma
print("Valor del atributo desde la clase: ", MiClase.varible_clase)

# Solo sera ligado al Objeto
objeto1.varible_clase = "Nuevo valor del atributo de clase"
print(objeto1.varible_clase)