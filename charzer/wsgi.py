import os
import sys
sys.path.append('/opt/bitnami/projects/charzer')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/projects/charzer/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "charzer.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()