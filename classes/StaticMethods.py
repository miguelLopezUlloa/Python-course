class StaticMethods:
    
    variable_clase = "Atributo de clase"
    
    def __init__(self):
        self.variable_instancia = "Variable instancia"
        #En este punto el atributo va a existir hasta que se cree un objeto
        
        
    
    # Como se puede ver, no se necesita ningun parametro
    @staticmethod
    def method_static():
        print("Estoy en el Metodo Estatico")
        print("El valor del atributo de clase es:",StaticMethods.variable_clase)
        #Desde un método no se puede acceder a un atributo de clase
        #print(StaticMethods.variable_clase)
        
        
    # Con esta forma, si se necesita un parametro en el metodo
    @classmethod
    def method_class(cls):
        print("Metodo de Clase:", str(cls))
        print("Usando cls para acceder al atributo de la clase:", cls.variable_clase)
        
        
    def method_instance(self):
        self.method_static()
        self.method_class()
        print("Atributo de clase con:", self.variable_clase)
        print("Variable de instancia:", self.variable_instancia)
        

StaticMethods.method_static()
StaticMethods.method_class()

print("*" *60)

objOne = StaticMethods()
objOne.method_instance()
