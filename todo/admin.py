from django.contrib import admin

from .models import ToDo

# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_filter = ('status', 'created_at', 'done_time')
    list_display = ('title', 'status', 'created_at', 'done_time')
    search_fields = ('title', 'description')
    ordering = ('-created_at', )

admin.site.register(ToDo, ToDoAdmin)