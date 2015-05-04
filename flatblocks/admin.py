from django.contrib import admin
from flatblocks.models import FlatBlock
from hvad.admin import TranslatableAdmin

class FlatBlockAdmin(TranslatableAdmin):
    ordering = ['slug', ]
    list_display = ('slug', 'header', 'all_translations')
    search_fields = ('slug', 'header', 'content')

admin.site.register(FlatBlock, FlatBlockAdmin)
