from django.contrib import admin

# Register your models here

from .models import *
from django.conf import settings

class QuarterMatchlInline(admin.TabularInline):
    model = QuarterMatch
    fields = ['match_map', 'score1', 'score2','matchNumber']
    extra = 0
    readonly_fields = ('matchNumber',)
    def has_delete_permission(self, request, obj=None):
        return False

class SemiMatchlInline(admin.TabularInline):
    model = SemiMatch
    fields = ['match_map', 'score1', 'score2','matchNumber']
    extra = 0
    readonly_fields = ('matchNumber',)
    def has_delete_permission(self, request, obj=None):
        return False

class FinalMatchlInline(admin.TabularInline):
    model = FinalMatch
    fields = ['match_map', 'score1', 'score2',]
    extra = 1
    def has_delete_permission(self, request, obj=None):
        return False

class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ['id','user']
    list_display = ('id','user') 
    list_display_links = ('id','user') 

    def has_add_permission(self, request):
        return False



class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'game')
    list_display_links = ('name', 'game')
    inlines = [QuarterMatchlInline, SemiMatchlInline, FinalMatchlInline]
    readonly_fields = ['winner']
    class Media:
        css = {
            'all': ('css/tournament.css',),
        }

class QuarterMatchAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class SemiMatchAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class FinalMatchAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(Game)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(QuarterMatch, QuarterMatchAdmin)
admin.site.register(SemiMatch, SemiMatchAdmin)
admin.site.register(FinalMatch, FinalMatchAdmin)