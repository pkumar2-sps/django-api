import django
from django.conf import settings

from web import settings as web_settings

def pytest_configure():
	settings.configure(**vars(web_settings))
	settings.ALLOWED_HOSTS+=['testserver']
	django.setup()
