from django.urls import path
from . import views

app_name = 'expatica'
urlpatterns = [
    path('', views.ExpaticaView.as_view(), name='jobs')
]