import psycopg2

def init_db():
    db_name = "clinic_db"
    db_user = "nare"
    db_password = "nare5697"
    db_host = "localhost"
    db_port = 5437
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {db_name} OWNER {db_user};")
        print(f"Database '{db_name}' created successfully.")
    except Exception as e:
        print(f"Error creating database: {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    init_db()

