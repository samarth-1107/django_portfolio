from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=""),
    path('', views.about_section, name=""),
    path('', views.services_section, name=""),
]
