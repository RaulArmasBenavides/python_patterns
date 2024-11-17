class CoffeeMachineState:
    """Estado base para la máquina de café."""
    def insert_coin(self, machine):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
    
    def select_coffee(self, machine):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
    
    def dispense_coffee(self, machine):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")


class NoCoinState(CoffeeMachineState):
    """Estado cuando no hay moneda insertada."""
    def insert_coin(self, machine):
        print("Moneda insertada. Puede seleccionar su café.")
        machine.set_state(machine.coin_inserted_state)

    def select_coffee(self, machine):
        print("Primero debe insertar una moneda.")

    def dispense_coffee(self, machine):
        print("Primero debe insertar una moneda.")


class CoinInsertedState(CoffeeMachineState):
    """Estado cuando hay una moneda insertada."""
    def insert_coin(self, machine):
        print("Ya hay una moneda insertada. Seleccione su café.")

    def select_coffee(self, machine):
        print("Café seleccionado. Preparando...")
        machine.set_state(machine.coffee_selected_state)

    def dispense_coffee(self, machine):
        print("Seleccione un café primero.")


class CoffeeSelectedState(CoffeeMachineState):
    """Estado cuando se seleccionó un café."""
    def insert_coin(self, machine):
        print("Espere a que el café actual se dispense.")

    def select_coffee(self, machine):
        print("Ya seleccionó un café. Espere a que se dispense.")

    def dispense_coffee(self, machine):
        print("Dispensando café. ¡Disfrútelo!")
        machine.set_state(machine.no_coin_state)


class CoffeeMachine:
    """Clase principal que actúa como el contexto de la máquina de café."""
    def __init__(self):
        self.no_coin_state = NoCoinState()
        self.coin_inserted_state = CoinInsertedState()
        self.coffee_selected_state = CoffeeSelectedState()

        self.current_state = self.no_coin_state  # Estado inicial

    def set_state(self, state):
        self.current_state = state

    def insert_coin(self):
        self.current_state.insert_coin(self)

    def select_coffee(self):
        self.current_state.select_coffee(self)

    def dispense_coffee(self):
        self.current_state.dispense_coffee(self)


# Programa principal
if __name__ == "__main__":
    machine = CoffeeMachine()

    machine.insert_coin()        # Moneda insertada
    machine.select_coffee()      # Selección de café
    machine.dispense_coffee()    # Dispensando café

    machine.dispense_coffee()    # Error: no hay moneda
