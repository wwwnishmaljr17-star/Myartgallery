import sqlite3
import os

db_path = 'db.sqlite3'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT username, password, type FROM MYAPP_logintbl")
        users = cursor.fetchall()
        print("Users in MYAPP_logintbl:")
        for user in users:
            print(f"Username: {user[0]}, Password: {user[1]}, Type: {user[2]}")
    except Exception as e:
        print(f"Error: {e}")
    conn.close()
else:
    print("db.sqlite3 not found")
