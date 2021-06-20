from django.contrib import admin

from .models import Details


class Assign(admin.ModelAdmin):
    fields = ['name', 'dob','email','number']

admin.site.register(Details, Assign)