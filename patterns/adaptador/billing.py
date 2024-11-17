# Sistema de Facturación existente
class BillingSystem:
    """Sistema de facturación que devuelve facturas como listas."""
    def generate_invoice(self):
        return ["Invoice001", "2024-11-16", 1500.00]  # [InvoiceID, Date, Amount]


# ERP que necesita datos en un formato específico
class ERPSystem:
    """ERP que requiere facturas en un formato JSON estructurado."""
    def process_invoice(self, invoice_data):
        print("Procesando factura en el ERP:")
        print(f"ID: {invoice_data['id']}")
        print(f"Fecha: {invoice_data['date']}")
        print(f"Monto: {invoice_data['amount']}")


# Adaptador
class BillingToERPAdapter:
    """Adaptador entre el Sistema de Facturación y el ERP."""
    def __init__(self, billing_system):
        self.billing_system = billing_system

    def get_invoice(self):
        """Traduce la factura generada por el sistema de facturación al formato esperado por el ERP."""
        invoice = self.billing_system.generate_invoice()
        # Transformar la lista en un formato JSON estructurado
        return {
            "id": invoice[0],
            "date": invoice[1],
            "amount": invoice[2]
        }


# Cliente empresarial
if __name__ == "__main__":
    # Instancia del sistema de facturación
    billing_system = BillingSystem()

    # Instancia del ERP
    erp_system = ERPSystem()

    # Adaptador para conectar ambos sistemas
    adapter = BillingToERPAdapter(billing_system)
    invoice_data = adapter.get_invoice()  # Traduce los datos

    # ERP procesa la factura traducida
    erp_system.process_invoice(invoice_data)
