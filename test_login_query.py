import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ART_GALLERY.settings')
django.setup()

from MYAPP.models import loginTbl

# Simulating inputs
uname = "Nishmal"
passw = "Nishmal.17"

# Test exact
print(f"Testing exact match for '{uname}'")
lo = loginTbl.objects.filter(username=uname, password=passw)
print(f"Filter(username='{uname}'): {lo.exists()}")

# Test iexact
print(f"Testing iexact match for '{uname}'")
lo = loginTbl.objects.filter(username__iexact=uname, password=passw)
print(f"Filter(username__iexact='{uname}'): {lo.exists()}")

# Check all
print("\nAll users in DB:")
for u in loginTbl.objects.all():
    print(f" - '{u.username}' (type: {u.type})")
