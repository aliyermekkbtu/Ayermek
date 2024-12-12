import psycopg2

def query_all_contacts():
    try:
        # Establishing the connection
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="24680ali",
            port="5432"
        )
        cur = conn.cursor()

        # Query to fetch all contacts
        cur.execute('SELECT "name", "number" FROM phonebook;')

        # Fetch all records
        contacts = cur.fetchall()

        # Displaying the contacts
        if contacts:
            print("Contacts in the phonebook:")
            for contact in contacts:
                print(f"name: {contact[0]}, number: {contact[1]}")
        else:
            print("No contacts found in the phonebook.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Closing the connection
        cur.close()
        conn.close()

# Example call
query_all_contacts()
