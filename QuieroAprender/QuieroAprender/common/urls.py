from django.urls import path

from QuieroAprender.common.views import home, country_details, about, university

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('university/', university, name='university'),
    path('country/<str:country_name>/', country_details, name='country_details'),
]