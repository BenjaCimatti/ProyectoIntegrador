from django.contrib import admin

# Register your models here

from .models import *

class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ["id","user"]

    

admin.site.register(Game)
#admin.site.register(Tournament)
admin.site.register(Player)
#admin.site.register(Match)