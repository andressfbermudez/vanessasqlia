from sqlalchemy import MetaData, text
from sqlalchemy.sql.ddl import CreateTable

from backend.llm.duckdb_nsql_service import duckdb_nsql_service


# Enviar el prompt al modelo de IA para generar la consulta SQL
def process_prompt_service(prompt, database):
    # Obtener el schema de la base de datos para contextulizar el modelo de IA
    engine = database.get_bind()
    database_schema = get_database_schema(engine)

    # Enviar el prompt al modelo de IA para obtener la query
    query = duckdb_nsql_service(prompt, database_schema)

    # Ejecutar la query generada por el modelo de IA (Solo se permiten SELECT)
    normalize_query = query.strip().upper().split()[0]
    if normalize_query in [
        "SELECT","SHOW", "DESCRIBE",
        "CREATE", "INSERT",
        "UPDATE", "ALTER",
        "DELETE", "DROP", "TRUNCATE"
    ]:
        response = execute_query_service(query.strip(), database)
        print("PROMPT:", prompt, " - ", "SQL:", query)
        return response
    else:
        print("PROMPT:", prompt, " - ", "SQL:", query)
        return "Este tipo de operaciones no estan permitidas por seguridad."


# Para obtener el schema de la base de datos
def get_database_schema(engine) -> str:
    """
    Extrae el esquema completo de la base de datos y lo devuelve como texto SQL.
    """
    metadata = MetaData()
    metadata.reflect(bind=engine)

    schema_text = []
    for table in metadata.sorted_tables:
        create_stmt = str(CreateTable(table).compile(engine))

        # Limpia detalles innecesarios
        clean_stmt = "\n".join(
            line for line in create_stmt.splitlines()
            if not line.strip().startswith("CONSTRAINT") and "FOREIGN KEY" not in line
        )
        schema_text.append(clean_stmt + ";")

    return "\n\n".join(schema_text)


# Ejecutar la query
def execute_query_service(sql_query, database):
    try:
        # Ejecutar la query
        result = database.execute(text(sql_query))
        database.commit()

        # Normalizar la query para determinar que tipo de operacion se realizo.
        normalized_query = sql_query.strip().upper()
        first_word = normalized_query.split()[0]

        # Determinar el tipo de respuesta segun el tipo de operacion ejecutada
        if first_word == "SELECT" or first_word == "SHOW" or first_word == "DESCRIBE":
            rows = [
                {key: str(value) if value is not None else "" for key, value in row._mapping.items()}
                for row in result
            ]
            return rows
        else:
            return "Operacion completada correctamente."

    # Capturar errores
    except Exception as e:
        print(f"Error al ejecutar la consulta SQL: {e}")
        return "Error en el servidor al realizar la operacion sobre la base de datos."
