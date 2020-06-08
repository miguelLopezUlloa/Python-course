class Person:

    def __init__(self, name, lastName, motherName):
        self.name = name
        # _ indica protected access
        self._lastName = lastName
        # __ indica private access
        self.__surName = motherName
    
    def __privateMethod(self):
        print(self.name)
        print(self._lastName)
        print(self.__surName)
      
    """ Se llama a un metodo privado desde un metodo publico """   
    def publicMethod(self):
        self.__privateMethod()
        
    def getLastName(self):
        return self._lastName
    
    def setLastName(self, lastName):
        self._lastName = lastName
        
    def getSurName(self):
        return self.__surName
    
    def setSurName(self, motherName):
        self.__surName = motherName
        
    
p1 = Person("Juan", "Lopez", "Perez")

#p1.publicMethod()
print(p1.getLastName());
print(p1.getSurName());

print("***********************************************")
p1.publicMethod()


