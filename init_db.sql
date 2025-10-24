CREATE TABLE IF NOT EXISTS max_cundapi (
    id SERIAL PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL
);

INSERT INTO max_cundapi (nombre_completo)
VALUES ('Maximiliano Cundapi Muñoa')
ON CONFLICT DO NOTHING;
