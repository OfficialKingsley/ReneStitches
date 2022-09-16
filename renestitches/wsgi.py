import os
import sys
from django.core.wsgi import get_wsgi_application

path = "/home/kingsleyjr/ReneStitches"
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "renestiches.settings"

# then:

application = get_wsgi_application()
