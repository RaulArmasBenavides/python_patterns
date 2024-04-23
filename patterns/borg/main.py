class Borg:
    _shared_state = {}
    
    def __init__(self):
        self.__dict__ = self._shared_state
        # inicializa cualquier otro estado deseado aquí

# Uso del Borg
b1 = Borg()
b2 = Borg()

b1.x = 4
b1.valor = 5
print(b2.x)  # Salida: 4, aunque nunca se asignó directamente a b2
print(b2.valor) #Salida : 5, aunque tampoco se asignó directamente a b2
