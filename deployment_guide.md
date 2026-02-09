# Deployment Guide (PythonAnywhere)

Follow these steps to host your **Art Gallery** project online.

## 1. Create a PythonAnywhere Account
1. Go to [PythonAnywhere](https://www.pythonanywhere.com/).
2. Sign up for a **Free** (Beginner) account.

## 2. Upload Your Code
1. Open a **Bash Console** on PythonAnywhere.
2. Clone your repository:
   ```bash
   git clone https://github.com/wwwnishmaljr17-star/Myartgallery.git
   cd Myartgallery
   ```

## 3. Set Up Virtual Environment
1. In the same Bash console, create a virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   pip install pymysql  # Driver for MySQL
   ```

## 4. Configure Database (MySQL)
1. Go to the **Databases** tab on PythonAnywhere.
2. Set a MySQL password and create a database named `artgallerys`.
3. In your `settings.py` (on PythonAnywhere), update the `DATABASES` section:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'yourusername$artgallerys',
           'USER': 'yourusername',
           'PASSWORD': 'yourmysqlpassword',
           'HOST': 'yourusername.mysql.pythonanywhere-services.com',
       }
   }
   ```

## 5. Configure Web App
1. Go to the **Web** tab.
2. Click **Add a new web app**.
3. Choose **Manual Configuration** (important!) and select **Python 3.10**.
4. Set the **Virtualenv** path to `/home/yourusername/.virtualenvs/myenv`.
5. Update the **WSGI configuration file** (link found in the Web tab):
   ```python
   import os
   import sys
   path = '/home/yourusername/Myartgallery'
   if path not in sys.path:
       sys.path.append(path)
   os.environ['DJANGO_SETTINGS_MODULE'] = 'ART_GALLERY.settings'
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

## 6. Static Files
1. In the **Web** tab, scroll down to **Static Files**.
2. Add a new entry:
   - URL: `/static/`
   - Path: `/home/yourusername/Myartgallery/staticfiles`
3. Add another entry for media:
   - URL: `/media/`
   - Path: `/home/yourusername/Myartgallery/media`

## 7. Run Collectstatic & Migrate
1. In your Bash console:
   ```bash
   python manage.py collectstatic --noinput
   python manage.py migrate
   ```

## 8. Reload & Visit
1. Go back to the **Web** tab and click **Reload**.
2. Visit your site at `yourusername.pythonanywhere.com`.
