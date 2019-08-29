from django.contrib import admin
from .models import Microrna
# Register your models here.
@admin.register(Microrna)
class MicrornaAdmin(admin.ModelAdmin):
	list_display = ('name', 'spename', 'chrosome' ,'sequence', 'length')