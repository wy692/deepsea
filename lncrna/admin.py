from django.contrib import admin
from .models import Lncrna
# Register your models here.
@admin.register(Lncrna)
class LncrnaAdmin(admin.ModelAdmin):
	list_display = ('name', 'spename', 'chrosome' ,'sequence', 'length')