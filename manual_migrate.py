import json
import sqlite3
import os

db_path = 'db.sqlite3'
json_path = 'data_utf8.json'

def migrate():
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Tables to migrate
    models = {
        'MYAPP.logintbl': 'MYAPP_logintbl',
        'MYAPP.artisttbl': 'MYAPP_artisttbl',
        'MYAPP.usertbl': 'MYAPP_usertbl',
        # Add more if needed
    }
    
    for entry in data:
        model_name = entry['model']
        if model_name in models:
            table_name = models[model_name]
            fields = entry['fields']
            pk = entry['pk']
            
            # Handle Foreign Keys - Django exports PKs directly
            # Ensure table names match what migrate created
            
            field_names = ['id'] + list(fields.keys())
            values = [pk] + list(fields.values())
            
            # Clean up field names for SQLite (e.g. rename 'LOGINID' to 'LOGINID_id')
            clean_field_names = []
            for f in field_names:
                if f == 'LOGINID' or f == 'USERID' or f == 'LOGIN' or f == 'PRODUCT' or f == 'ORDER':
                    clean_field_names.append(f + '_id')
                else:
                    clean_field_names.append(f)

            placeholders = ', '.join(['?'] * len(values))
            query = f"INSERT OR REPLACE INTO {table_name} ({', '.join(clean_field_names)}) VALUES ({placeholders})"
            
            try:
                cursor.execute(query, values)
            except Exception as e:
                print(f"Error inserting into {table_name}: {e}")
                
    conn.commit()
    conn.close()
    print("Migration complete!")

if __name__ == "__main__":
    migrate()
