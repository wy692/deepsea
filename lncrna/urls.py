from django.urls import path
from . import views
urlpatterns = [
	path('',views.lncrna,name='lncrna'),
]