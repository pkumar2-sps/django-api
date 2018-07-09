import django
from django.conf import settings

from label_service_api import settings as label_service_api_settings

def pytest_configure():
	settings.configure(**vars(label_service_api_settings))
	settings.ALLOWED_HOSTS+=['testserver']
	django.setup()