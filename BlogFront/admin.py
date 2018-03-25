from django.contrib import admin
from BlogFront.models import NoteName


class NoteNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'creat_time']


admin.site.register(NoteName, NoteNameAdmin)
