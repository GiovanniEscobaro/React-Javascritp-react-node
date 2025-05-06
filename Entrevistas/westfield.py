import smtplib
from datetime import datetime, timedelta

def enviar_correo(destinatario, asunto, mensaje):
    # Código para enviar correo usando smtplib o un servicio como SendGrid
    pass

def verificar_pagos(pagos):
    hoy = datetime.now()
    
    for pago in pagos:
        fecha_pago = pago['fecha_pago']
        estado_pago = pago['estado_pago']
        email = pago['email']
        
        # Calcular diferencia en días
        diferencia_dias = (hoy - fecha_pago).days
        
        if diferencia_dias == 3 and estado_pago == 'pendiente':
            enviar_correo(email, "Recordatorio: Pago pendiente", "Faltan 3 días para su fecha de pago")
        elif diferencia_dias == 2 and estado_pago == 'pendiente':
            enviar_correo(email, "Cobro de cartera", "Han pasado 2 días desde la fecha de pago")
        elif diferencia_dias == 15 and estado_pago == 'pendiente':
            enviar_correo(email, "Aviso importante", "Por no haber realizado el pago, perderá acceso a la plataforma")

# Ejemplo de uso
pagos = [
    {'email': 'cliente1@example.com', 'fecha_pago': datetime(2025, 4, 25), 'estado_pago': 'pendiente'},
    {'email': 'cliente2@example.com', 'fecha_pago': datetime(2025, 4, 15), 'estado_pago': 'pendiente'}
]
verificar_pagos(pagos)
