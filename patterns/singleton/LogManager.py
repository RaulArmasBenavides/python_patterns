import logging

class LogManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Inicializando gestor de logs.")
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.logger = logging.getLogger("AppLogger")
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s - %(message)s")
            handler.setFormatter(formatter)
            cls._instance.logger.addHandler(handler)
            cls._instance.logger.setLevel(logging.INFO)
        return cls._instance

    def get_logger(self):
        return self.logger

# Uso
logger1 = LogManager().get_logger()
logger2 = LogManager().get_logger()
logger1.info("Primer mensaje de log.")
logger2.info("Segundo mensaje de log.")
logger1.info("Test test test test")
