import os
import sys

# Calculate the path based on the location of the WSGI script.
FILE_PATH = os.path.dirname(__file__)
FRAGASTATEN_PATH = os.path.dirname(FILE_PATH)
PROJECT_PATH = os.path.join(FRAGASTATEN_PATH, '..')
sys.path.append(FRAGASTATEN_PATH)
sys.path.append(PROJECT_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fragastaten.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()

try:
    from dj_static import Cling
    application = Cling(application)
except ImportError:
    pass
