from django.contrib import admin
from .models import *
# Register your models here.
class PoolAdmin(admin.ModelAdmin):
    list_display = ('pool_name','pool_tier', 'pool_access','swap_amount','pool_status')
    list_editable = ('pool_status',)
    search_fields = ('pool_name', 'pool_access','swap_amount', 'pool_status')
    list_per_page = 25
    list_filter = ('pool_name','pool_tier','pool_status',)

class WhitelistAdmin(admin.ModelAdmin):
    list_display = ('pool_name', 'eth_adddress')
    search_fields = ('pool_name', 'eth_adddress')
    list_per_page = 25
    list_filter = ('pool_name',)


admin.site.register(Pool, PoolAdmin)
admin.site.register(Whitelist, WhitelistAdmin)

