import sqlite3
import os

db_path = 'db.sqlite3'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password, type FROM MYAPP_logintbl")
    users = cursor.fetchall()
    print("--- HEX DEBUG ---")
    for user in users:
        u_name = user[0]
        u_pass = user[1]
        u_type = user[2]
        print(f"User: '{u_name}' | Hex: {u_name.encode().hex()}")
        print(f"Pass: '{u_pass}' | Hex: {u_pass.encode().hex()}")
        print(f"Type: '{u_type}'")
        print("-" * 20)
    conn.close()
else:
    print("db.sqlite3 not found")
