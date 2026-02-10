import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ART_GALLERY.settings')
django.setup()

from MYAPP.models import loginTbl

# Create a default admin if it doesn't exist
if not loginTbl.objects.filter(username='admin').exists():
    loginTbl.objects.create(username='admin', password='adminpassword', type='admin')
    print("Admin user created: admin / adminpassword")

# Create a default artist if it doesn't exist
if not loginTbl.objects.filter(username='artist').exists():
    loginTbl.objects.create(username='artist', password='artistpassword', type='artist')
    print("Artist user created: artist / artistpassword")
else:
    print("Accounts already exist.")
