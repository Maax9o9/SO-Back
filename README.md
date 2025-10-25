Servicios Incluidos
1. Frontend (HTML, CSS y JavaScript)

Muestra el nombre del autor: Max Cundapi.

Consume datos desde la API REST mediante fetch.

Se ejecuta en el puerto 80.

Construido desde un Dockerfile personalizado (sin usar nginx).

Comunicación interna con el backend usando el nombre del servicio (backend_cundapi).

Comando interno de ejecución:

python3 -m http.server 80

2. Backend (FastAPI)

API REST desarrollada en Python FastAPI.

Expone el puerto 8000.

Se conecta a la base de datos PostgreSQL.

Incluye el endpoint /cundapi, que devuelve el nombre completo del autor:

{"nombre_completo": "Maximiliano Cundapi Muñoa"}


Configurado mediante variables de entorno (POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB).

3. Base de Datos (PostgreSQL)

Base de datos: max_db

Usuario: max_user

Contraseña: max_pass

Puerto: 5432

Se inicializa con el script init_db.sql

Mantiene persistencia con el volumen pgdata:/var/lib/postgresql/data

Arquitectura General
┌───────────────────┐        ┌──────────────────┐        ┌────────────────────┐
│   FRONTEND (80)   │  --->  │  BACKEND (8000)  │  --->  │  POSTGRES (5432)   │
│ HTML + JS (fetch) │        │   FastAPI REST   │        │  max_db persistente │
└───────────────────┘        └──────────────────┘        └────────────────────┘
           ↑                            ↑
           │                            │
     Navegador web                Red interna Docker

Docker Compose

El proyecto define tres servicios interconectados mediante una red interna (red_cundapi).

Archivo docker-compose.yml (resumen):

services:
  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      POSTGRES_HOST: db
      POSTGRES_DB: max_db
      POSTGRES_USER: max_user
      POSTGRES_PASSWORD: max_pass

  db:
    image: postgres:15
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: max_db
      POSTGRES_USER: max_user
      POSTGRES_PASSWORD: max_pass
    volumes:
      - ./backend/init_db.sql:/docker-entrypoint-initdb.d/init_db.sql
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
networks:
  red_cundapi:
    driver: bridge

Cómo levantar el entorno

Clonar el repositorio:

git clone https://github.com/TU_USUARIO/proyecto_ms_max.git
cd proyecto_ms_max


Construir las imágenes:

sudo docker-compose build


Levantar los contenedores:

sudo docker-compose up -d


Verificar que estén corriendo:

sudo docker ps

Accesos desde navegador
Servicio	URL pública EC2 (ejemplo)	Puerto
Frontend	http://34.204.132.72
	80
Backend	http://34.204.132.72:8000
	8000
Endpoint /cundapi	http://34.204.132.72:8000/cundapi
	-
Persistencia

Los datos de PostgreSQL se almacenan en un volumen persistente (pgdata), lo que garantiza que la información no se pierda incluso al reiniciar los contenedores.

Comandos útiles
Acción	Comando
Ver logs	sudo docker-compose logs -f
Detener contenedores	sudo docker-compose down
Reiniciar servicios	sudo docker-compose up -d
Reconstruir imágenes	sudo docker-compose build
Autor

Maximiliano Cundapi Muñoa
Proyecto individual — Arquitectura de Microservicios
Universidad Politécnica de Chiapas
