from django.contrib import admin
from .models import Languages,Technical,Music


class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'place', 'description')


class TechnicalAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'place', 'description')


class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'place', 'description')


admin.site.register(Music,MusicAdmin)
admin.site.register(Technical,TechnicalAdmin)
admin.site.register(Languages,LanguagesAdmin)
