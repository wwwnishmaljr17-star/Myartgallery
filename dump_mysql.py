import MySQLdb

try:
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="yourpassword",
        db="artgallerys"
    )
    cursor = db.cursor()
    cursor.execute("SELECT username, password FROM MYAPP_logintbl WHERE type = 'artist' LIMIT 1")
    res = cursor.fetchone()
    if res:
        print(f"Artist Found: {res[0]} / {res[1]}")
    else:
        print("No Artist found in local MySQL.")
    db.close()
except Exception as e:
    print(f"Error: {e}")
