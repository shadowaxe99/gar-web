
from django.contrib import admin
from .models import NFT

@admin.register(NFT)
class NFTAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner')
    search_fields = ('name', 'owner')
