import sqlite3

def insecure_query(user_input):
    # Vulnerable to SQL injection
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    print(cursor.fetchall())

# Simulate a malicious user input
user_input = "' OR '1'='1"
insecure_query(user_input)

