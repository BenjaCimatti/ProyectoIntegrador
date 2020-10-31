from django.contrib import admin

# Register your models here

from .models import *

class QuarterMatchlInline(admin.TabularInline):
    model = QuarterMatch
    fields = ['match_map',]
    extra = 4

class SemiMatchlInline(admin.TabularInline):
    model = SemiMatch
    fields = ['match_map',]
    extra = 2

class FinalMatchlInline(admin.TabularInline):
    model = FinalMatch
    fields = ['match_map',]
    extra = 1

class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ["id","user"]

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'game')
    list_display_links = ('name', 'game')
    inlines = [QuarterMatchlInline, SemiMatchlInline, FinalMatchlInline]

    

admin.site.register(Game)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Player)
admin.site.register(QuarterMatch)
admin.site.register(SemiMatch)
admin.site.register(FinalMatch)