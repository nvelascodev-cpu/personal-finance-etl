CREATE_TRANSACTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS transactions (

    id INTEGER PRIMARY KEY,

    fecha TEXT,

    tipo TEXT,

    categoria TEXT,

    descripcion TEXT,

    monto REAL,

    modo_pago TEXT

);
"""