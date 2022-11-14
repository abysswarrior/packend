from django.urls import path
from . import views

app_name = 'relocateme'
urlpatterns = [
    path('', views.RelocateMeView.as_view(), name='jobs')
]