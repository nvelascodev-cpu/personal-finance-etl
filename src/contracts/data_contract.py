COLUMNS = [
    "id",
    "fecha",
    "tipo",
    "categoria",
    "descripcion",
    "monto",
    "modo_pago"
]

EXPECTED_TYPES = {
    "id": "Int64",
    "fecha": "datetime",
    "tipo": "string",
    "categoria": "string",
    "descripcion": "string",
    "monto": "float64",
    "modo_pago": "string"
}

VALID_VALUES = {
    "modo_pago": [
        "Efectivo",
        "Transferencia",
        "Tarjeta"
    ]
}