from __future__ import annotations
from abc import ABC, abstractmethod


# ---------------------------
# Implementor (Bridge side)
# ---------------------------
class NotificationSender(ABC):
    @abstractmethod
    def send(self, to: str, subject: str, body: str) -> None:
        """Low-level sending operation (channel/provider details)."""
        raise NotImplementedError


class EmailSender(NotificationSender):
    def send(self, to: str, subject: str, body: str) -> None:
        # Aquí iría tu integración real (SMTP/SendGrid/etc.)
        print(f"[EMAIL] To={to} | Subject={subject} | Body={body}")


class SmsSender(NotificationSender):
    def send(self, to: str, subject: str, body: str) -> None:
        # subject puede ser ignorado en SMS, pero lo mantenemos por interfaz uniforme
        print(f"[SMS] To={to} | Body={body}")


class PushSender(NotificationSender):
    def send(self, to: str, subject: str, body: str) -> None:
        print(f"[PUSH] To={to} | Title={subject} | Body={body}")


# ---------------------------
# Abstraction
# ---------------------------
class Notification(ABC):
    def __init__(self, sender: NotificationSender) -> None:
        self._sender = sender  # Bridge: composition over inheritance

    @abstractmethod
    def notify(self, to: str) -> None:
        """High-level notification behavior."""
        raise NotImplementedError

    # Opcional: permitir cambiar el implementor en runtime
    def set_sender(self, sender: NotificationSender) -> None:
        self._sender = sender


# ---------------------------
# Refined Abstractions
# ---------------------------
class AlertNotification(Notification):
    def __init__(self, sender: NotificationSender, message: str) -> None:
        super().__init__(sender)
        self._message = message

    def notify(self, to: str) -> None:
        subject = "ALERTA"
        body = self._message
        self._sender.send(to=to, subject=subject, body=body)


class InvoiceNotification(Notification):
    def __init__(self, sender: NotificationSender, invoice_id: str, amount: float) -> None:
        super().__init__(sender)
        self._invoice_id = invoice_id
        self._amount = amount

    def notify(self, to: str) -> None:
        subject = f"Factura {self._invoice_id}"
        body = f"Se generó la factura {self._invoice_id} por S/ {self._amount:.2f}."
        self._sender.send(to=to, subject=subject, body=body)


# ---------------------------
# Example usage
# ---------------------------
if __name__ == "__main__":
    email = EmailSender()
    sms = SmsSender()
    push = PushSender()

    alert = AlertNotification(email, "Se detectó un inicio de sesión sospechoso.")
    alert.notify("raul@dominio.com")

    # Cambiar el canal/implementación sin cambiar la abstracción
    alert.set_sender(sms)
    alert.notify("+51999999999")

    invoice = InvoiceNotification(push, "INV-2026-0001", 199.90)
    invoice.notify("user_device_token_abc123")
