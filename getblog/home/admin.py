from os import O_TEMPORARY
from django.contrib import admin
from .models import Contact

# Register your models here.
admin.site.register(Contact)