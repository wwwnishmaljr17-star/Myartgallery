# Deployment Guide (Free Hosting - SQLite)

Since MySQL is a paid feature on PythonAnywhere, we have switched your project to use **SQLite** (which is free and built-in). Follow these simple steps to get your site live.

## 1. Update Your Code on PythonAnywhere
If you already cloned the code, run these commands in your **Bash Console**:
```bash
cd Myartgallery
git pull origin main
```

## 2. Set Up Virtual Environment (If not done)
If you haven't set up the environment yet:
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install -r requirements.txt
```

## 3. Configure Web App
1. Go to the **Web** tab.
2. Click **Add a new web app**.
3. Choose **Manual Configuration** -> **Python 3.10**.
4. Set **Virtualenv** to `/home/nishmal/.virtualenvs/myenv`.
5. Click **WSGI configuration file** and paste this:
   ```python
   import os
   import sys
   path = '/home/nishmal/Myartgallery'
   if path not in sys.path:
       sys.path.append(path)
   os.environ['DJANGO_SETTINGS_MODULE'] = 'ART_GALLERY.settings'
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

## 4. Static Files
In the **Web** tab, scroll to **Static Files**:
- URL: `/static/` | Path: `/home/nishmal/Myartgallery/staticfiles`
- URL: `/media/`  | Path: `/home/nishmal/Myartgallery/media`

## 5. Initialize the Site
In your **Bash Console**, run:
```bash
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser  # Create your admin account
```

## 6. Reload
Go back to the **Web** tab and click the big green **Reload** button.
Visit: `nishmal.pythonanywhere.com`
