from django.contrib import admin

# Register your models here.

from models import Persona, Tweet

admin.site.register(Persona)
admin.site.register(Tweet)