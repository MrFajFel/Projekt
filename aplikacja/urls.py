from django.urls import path

from aplikacja import views

app_name = 'aplikacja'

urlpatterns = [
    path('', views.note_list, name='note_list')
]