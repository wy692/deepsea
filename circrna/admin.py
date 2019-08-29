from django.contrib import admin
from .models import Circrna
# Register your models here.
@admin.register(Circrna)
class CircrnaAdmin(admin.ModelAdmin):
	list_display = ('name', 'spename', 'chrosome' ,'sequence', 'length')