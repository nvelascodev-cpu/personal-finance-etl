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
    "id": "int64",
    "fecha": "string",
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