from abc import ABC, abstractmethod


# Mediador abstracto
class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message, sender):
        pass

    @abstractmethod
    def add_user(self, user):
        pass


# Mediador concreto
class ChatRoom(ChatMediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            # El emisor no recibe su propio mensaje
            if user != sender:
                user.receive_message(message, sender)


# Clase base para usuarios
class User(ABC):
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def receive_message(self, message, sender):
        pass


# Usuario concreto
class ChatUser(User):
    def send_message(self, message):
        print(f"{self.name} envía: {message}")
        self.mediator.send_message(message, self)

    def receive_message(self, message, sender):
        print(f"{self.name} recibe de {sender.name}: {message}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear mediador
    chat_room = ChatRoom()

    # Crear usuarios
    user1 = ChatUser("Alice", chat_room)
    user2 = ChatUser("Bob", chat_room)
    user3 = ChatUser("Charlie", chat_room)

    # Registrar usuarios en el chat
    chat_room.add_user(user1)
    chat_room.add_user(user2)
    chat_room.add_user(user3)

    # Interacción entre usuarios
    user1.send_message("Hola a todos!")
    user2.send_message("¡Hola Alice!")
    user3.send_message("Buenas a todos.")
