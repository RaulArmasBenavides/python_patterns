class HotelMediator:
    def notify(self, sender, event):
        pass

class ConcreteHotelMediator(HotelMediator):
    def __init__(self):
        self.reservation_system = None
        self.housekeeping = None
        self.customer_service = None
    
    def notify(self, sender, event):
        if event == "reservation_made":
            print("Notifying housekeeping to prepare the room.")
            self.housekeeping.prepare_room()
            print("Notifying customer service for guest preferences.")
            self.customer_service.handle_preferences()
        elif event == "room_cleaned":
            print("Room cleaned, notifying reservation system to update room status.")
            self.reservation_system.update_room_status()

class BaseHotelComponent:
    def __init__(self, mediator=None):
        self.mediator = mediator

class ReservationSystem(BaseHotelComponent):
    def make_reservation(self):
        print("Reservation made for a room.")
        self.mediator.notify(self, "reservation_made")

    def update_room_status(self):
        print("Reservation system updating room status to available.")

class Housekeeping(BaseHotelComponent):
    def prepare_room(self):
        print("Housekeeping is preparing the room.")
        self.mediator.notify(self, "room_cleaned")

class CustomerService(BaseHotelComponent):
    def handle_preferences(self):
        print("Customer service is handling guest preferences based on the reservation.")

if __name__ == "__main__":
    # Create the mediator
    mediator = ConcreteHotelMediator()
    
    # Create the components
    reservation = ReservationSystem(mediator)
    housekeeping = Housekeeping(mediator)
    customer_service = CustomerService(mediator)
    
    # Assign components to the mediator
    mediator.reservation_system = reservation
    mediator.housekeeping = housekeeping
    mediator.customer_service = customer_service
    
    # Simulate a room reservation
    reservation.make_reservation()
