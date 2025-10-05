import ollama

# Servicio para hacer peticiones al modelo de IA por medio de OLLAMA
def duckdb_nsql_service(prompt: str, database_schema: str) -> str:
    """
    Envía un prompt a Ollama utilizando el modelo duckdb-nsql y devuelve la consulta SQL generada.

    :param prompt: Pregunta en lenguaje natural.
    :param database_schema: Esquema de la base de datos en formato SQL.
    :return: Consulta SQL generada por el modelo.
    """
    try:
        result = ollama.generate(
            model='duckdb-nsql',
            system=f'This is the schema of my MYSQL database: {database_schema}',
            prompt=prompt
        )
        return result.response
    except Exception as e:
        print(f"Error al generar la consulta SQL: {e}")
        return ""
