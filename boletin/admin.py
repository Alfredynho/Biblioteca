from django.contrib import admin
from .models import Registrado
# Registrando los modelos

class AdminRegistrado(admin.ModelAdmin):
	list_display = ['__str__','nombre','timestamp']
	class Meta:
		model = Registrado

admin.site.register(Registrado,AdminRegistrado)