from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nation', 'reset', 'phone', 'money', 'textHint', 'timer', 'pause', 'answer']


admin.site.register(Profile, ProfileAdmin)
