from django.urls import include, path, re_path
from . import views

# app_name = "label_api"

urlpatterns = [

    path('api/v1/reports/<int:limit>/', view=views.SimpleExample.as_view(), name='report'),
    re_path(r'^api/v1/reports/(?P<limit>\w{0,50})$', view=views.SimpleExample.as_view(), name='re_report'),
    # path('image/', view=views.get_image, name='get_image'),

]
