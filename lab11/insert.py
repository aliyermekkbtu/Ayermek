import psycopg2

def add_contact():
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

        # Taking user input
        name = input("Enter the person's name: ")
        phone_number = input("Enter the person's phone number: ")

        # Inserting the contact into the table
        cur.execute('''
            INSERT INTO phonebook ("name", "number")
            VALUES (%s, %s);
        ''', (name, phone_number))

        # Commit the transaction
        conn.commit()
        print(f"Contact {name} added successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Closing the connection
        cur.close()
        conn.close()

# Example call
add_contact()
