from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Datos de conexión al servidor MySQL
DB_SERVER = "localhost:3306"
DB_USERNAME = "root"
DB_PASSWORD = "root"
DB_NAME = "development_db"

# URL de conexión a MySQL
DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa
Base = declarative_base()

# Proporciona una sesión de base de datos para una solicitud y la cierra al finalizar
def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
