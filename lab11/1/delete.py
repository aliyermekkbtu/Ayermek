import psycopg2
from config import host, user, password, db_name

def check_table_exists(connection, table_name):
    """
    Checks if a table exists in the database.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT to_regclass('{table_name}');")
            result = cursor.fetchone()
            return result[0] is not None
    except Exception as ex:
        print("[INFO] Error checking table existence:", ex)
        return False

def delete_data_by_name_or_phone(name, surname):
    """
    Deletes rows from the 'phonebook' table where 'name' matches 'name'
    or 'phone' matches 'phone'.
    """
    sql = """DELETE FROM phonebook WHERE name = %s OR surname = %s;"""

    try:
        # Establish the database connection
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        # Check if the table exists
        if not check_table_exists(connection, "phonebook"):
            print("[INFO] The table 'phonebook' does not exist.")
            return

        # Execute the SQL query using a cursor
        with connection.cursor() as cursor:
            cursor.execute(sql, (name, surname))
            print(f"[INFO] Deleted {cursor.rowcount} row(s).")

    except Exception as ex:
        print("[INFO] Error:", ex)

    finally:
        # Close the connection
        if connection:
            connection.close()

# Example Usage
if __name__ == "__main__":
    name_to_delete = "nas"
    surname_to_delete = "ahma"

    print(f"Attempting to delete rows where name='{name_to_delete}' or surname='{surname_to_delete}'...")
    delete_data_by_name_or_phone(name_to_delete, surname_to_delete)

