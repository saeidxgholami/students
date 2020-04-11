from django.urls import path

from . import views



urlpatterns = [
	path('', views.home),
	path('person/', views.save_person, name="person")
]