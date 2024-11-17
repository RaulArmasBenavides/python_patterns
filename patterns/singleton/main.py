from LogManager import LogManager
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.
    logger = LogManager().get_logger()
    logger.info("Usando LogManager en otro archivo.")
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        logger.info("Singleton works, both variables contain the same instance..")
    else:
        logger.info("Singleton failed, variables contain different instances..")