from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.RelocateMeView.as_view(), name='relocateme')
]