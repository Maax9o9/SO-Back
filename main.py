from fastapi import FastAPI
import psycopg2
import os

app = FastAPI(title="API Max Cundapi")

# Configuración de conexión a PostgreSQL
DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "db"),  # nombre del contenedor en Docker
    "database": os.getenv("POSTGRES_DB", "max_db"),
    "user": os.getenv("POSTGRES_USER", "max_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "max_pass"),
}

@app.get("/")
def root():
    return {"message": "Backend de Max Cundapi funcionando correctamente 🚀"}

@app.get("/cundapi")
def get_name():
    """Endpoint que devuelve el nombre completo desde la base de datos"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT nombre_completo FROM max_cundapi LIMIT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return {"nombre_completo": result[0] if result else "No hay datos"}
    except Exception as e:
        return {"error": str(e)}
