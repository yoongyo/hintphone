from django.contrib import admin
from .models import Theme, RoomEscape


class RoomEscapeAdmin(admin.ModelAdmin):
    list_display = ['name']


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(RoomEscape, RoomEscapeAdmin)
admin.site.register(Theme, ThemeAdmin)