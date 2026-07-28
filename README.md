# Personal Finance ETL

Proyecto de práctica desarrollado para ejemplificar los fundamentos de un proceso **ETL (Extract, Transform, Load)** utilizando **Python, Pandas y SQLite**.

El proyecto toma un archivo CSV con movimientos financieros personales, analiza su calidad, aplica transformaciones básicas y finalmente carga la información en una base de datos SQLite para su posterior consulta.

---

## Objetivos

- Ejemplificar la arquitectura de un proceso ETL.
- Trabajar con DataFrames usando Pandas.
- Aplicar transformaciones de limpieza de datos.
- Cargar información en una base de datos SQLite.
- Comprender la separación de responsabilidades entre Extract, Analyze, Transform y Load.

---

## Tecnologías utilizadas

- Python
- Pandas
- SQLite
- Git
- GitHub

---

## Estructura del proyecto

```
personal-finance-etl/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│
├── src/
│   ├── analysis/
│   ├── contracts/
│   ├── etl/
│   │   ├── extract/
│   │   ├── transform/
│   │   └── load/
│   └── utils/
│
├── tests/
│
├── requirements.txt
├── README.md
└── main.py
```

---

## Flujo del ETL

```
CSV
 │
 ▼
Extract
 │
 ▼
Analyze
 │
 ▼
Transform
 │
 ▼
Load
 │
 ▼
SQLite
 │
 ▼
Read Database
```

---

## Funcionalidades implementadas

### Extract

- Lectura del archivo CSV mediante Pandas.

### Analyze

- Perfil general del DataFrame.
- Conteo de filas y columnas.
- Tipos de datos.
- Valores nulos.
- Registros duplicados.
- Valores inválidos según el contrato de datos.

### Transform

- Eliminación de espacios innecesarios.
- Normalización de texto.
- Eliminación de filas completamente vacías.
- Eliminación de registros sin ID.
- Eliminación de IDs duplicados (conservando el primero).

### Load

- Conexión a SQLite.
- Creación automática de la tabla.
- Limpieza de la tabla para pruebas.
- Inserción de registros.
- Adaptación de tipos de datos compatibles con SQLite.
- Lectura de validación desde la base de datos.

---

## Base de datos

Motor utilizado:

- SQLite

Tabla principal:

- `personal_finance`

---

## Ejecución

Ejecutar desde la raíz del proyecto:

```bash
python main.py
```

---

## Enseñanzas 

Durante este proyecto se practican conceptos como:

- Arquitectura ETL.
- Manipulación de datos con Pandas.
- Consultas SQL básicas.
- Integración entre Python y SQLite.
- Organización modular de proyectos Python.
- Uso de Git y GitHub.
- Separación de responsabilidades entre las diferentes etapas del ETL.

---

## Estado del proyecto

✅ Proyecto finalizado como práctica de aprendizaje.

