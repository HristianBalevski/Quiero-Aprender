from django.urls import path

from QuieroAprender.common.views import index, country_details

urlpatterns = [
    path('', index, name='index'),
    path('country/<str:country_name>/', country_details, name='country_details'),
]