import psycopg2
from config import *

def insert_list(table_name):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        sql = """INSERT INTO phonebook (name, number) VALUES (%s, %s);"""
        with connection.cursor() as cursor:
                cursor.execute(sql, (name, number))
                print(f"[INFO] Successfully inserted: Name={name}, Number={number}")
    except Exception as ex:
            print("[INFO] Error inserting data:", ex)
    finally:
            connection.close()

        
