from django.contrib import admin
from .models import Theme


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name', 'roomEscape']


admin.site.register(Theme, ThemeAdmin)