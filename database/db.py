import psycopg2
from config.settings import settings


def selectFromDb():

    try:
        conn = psycopg2.connect(
            dbname=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
        )
        print("Connexion réussie !")

        cur = conn.cursor()
        cur.execute("SELECT * from films;")
        print(cur.fetchone())
        print(cur.fetchone())

        cur.close()
        conn.close()

    except Exception as e:
        print("Erreur :", e)
