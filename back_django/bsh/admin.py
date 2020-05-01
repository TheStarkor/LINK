from django.contrib import admin
from bsh.models import Bsh

class BshAdmin(admin.ModelAdmin):
    list_display=('title','author','created',)

admin.site.register(Bsh, BshAdmin)