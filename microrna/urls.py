from django.urls import path
from . import views
urlpatterns = [
	path('',views.microrna,name='microrna'),
]