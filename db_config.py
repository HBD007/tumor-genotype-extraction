import psycopg2
from psycopg2.extras import execute_values

def get_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432,
    )

def init_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS tumor_genotypes (
                id SERIAL PRIMARY KEY,
                patient_id TEXT,
                gene TEXT,
                variant TEXT,
                source_file TEXT
            );
            """)
            conn.commit()

def insert_genotypes(records):
    with get_connection() as conn:
        with conn.cursor() as cur:
            execute_values(cur, """
            INSERT INTO tumor_genotypes (patient_id, gene, variant, source_file)
            VALUES %s
            """, records)
            conn.commit()
