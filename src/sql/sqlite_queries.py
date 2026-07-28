CREATE_TRANSACTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS personal_finance (

    id INTEGER PRIMARY KEY,

    fecha TEXT,

    tipo TEXT,

    categoria TEXT,

    descripcion TEXT,

    monto REAL,

    modo_pago TEXT

);
"""

INSERT_DATAFRAME = """
INSERT INTO personal_finance (
    id,
    fecha,
    tipo,
    categoria,
    descripcion,
    monto,
    modo_pago
)
VALUES (?,?,?,?,?,?,?)

"""

READ_PERSONAL_FINANCE = """
SELECT *
FROM personal_finance 
"""

DELETE_TABLE = """
DELETE FROM personal_finance
"""