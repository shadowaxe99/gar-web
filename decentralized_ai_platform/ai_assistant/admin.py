
from django.contrib import admin
from .models import AiAssistant

@admin.register(AiAssistant)
class AiAssistantAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('-created_at',)
