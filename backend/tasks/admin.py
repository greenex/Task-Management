from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'due_date', 'completed')
    list_filter = ('completed', 'due_date')
    search_fields = ('name', 'owner__username')
    ordering = ('due_date',)
