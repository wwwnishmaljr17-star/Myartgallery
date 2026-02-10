import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ART_GALLERY.settings')
django.setup()

from MYAPP.models import loginTbl, artistTbl, userTbl

def load_data():
    # Use Sig to ignore BOM if present
    with open('data_utf8.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    for entry in data:
        model = entry['model']
        pk = entry['pk']
        fields = entry['fields']
        
        if model == 'MYAPP.logintbl':
            loginTbl.objects.update_or_create(id=pk, defaults=fields)
        elif model == 'MYAPP.artisttbl':
            # Handle FK
            login_id = fields.pop('LOGINID')
            artistTbl.objects.update_or_create(id=pk, LOGINID_id=login_id, defaults=fields)
        elif model == 'MYAPP.usertbl':
            login_id = fields.pop('LOGIN')
            userTbl.objects.update_or_create(id=pk, LOGIN_id=login_id, defaults=fields)
    
    print("Restore complete for MYAPP tables!")

if __name__ == "__main__":
    load_data()
